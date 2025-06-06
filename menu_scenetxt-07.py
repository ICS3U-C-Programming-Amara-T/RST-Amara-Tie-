#!/usr/bin/env python3
# Created by: Amara Tie 
# Date: May 28, 2025
# This program displays our opening message

import ugame
import stage
import constants
# menu scene function
def menu_scene():

    # Background image
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    # Displayed text on the Menu Screen 
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # Sets background size (10 x 8 and 16 x 16)
    background = stage.Grid(image_bank_mt_background,constants.SCREEN_X, constants.SCREEN_Y)
    # Set the frame to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # Set the images that will show up
    game.layers = text + [background]
    # Render background
    game.render_block()

    while True: 
        # gets the user input
        keys = ugame.buttons.get_pressed()
        # Sets start key to open the game scene function
        if keys & ugame.K_START != 0:
            game_scene()
        # redraw sprites
        game.tick()
        
# main game scene function
def game_scene():
    # Background image
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # button states
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
    # pew sounds
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # Sets background size (10 x 8 and 16 x 16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_X)
    # Sprites
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    alien = stage.Sprite(image_bank_sprites, 9, int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2), 16)
    
    # Set the frame to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # Set the images that will show up
    game.layers = [ship] + [alien] + [background]

    # Render background
    game.render_block()

    while True: 
        # gets the user input
        keys = ugame.buttons.get_pressed()
        # A button pressed states
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else: 
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        # B button pressed 
        if keys & ugame.K_O != 0:
            pass
        if keys & ugame.K_START != 0:
            print("Start")
            
        if keys & ugame.K_SELECT != 0:
            print("Select")
            
        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)
                
        if keys & ugame.K_LEFT != 0:
            if ship.x >= 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)
                
        if keys & ugame.K_UP != 0:
            pass
            
        if keys & ugame.K_DOWN != 0:
            pass
        # This plays the sound only when the A button is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
            
        # Redraw Sprite
        game.render_sprites([ship] + [alien])
        game.tick()
        


if __name__ == "__main__":
    menu_scene()