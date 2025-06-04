#!/usr/bin/env python3
# Created by: Amara Tie 
# Date: May 28, 2025
# This is my game program

import ugame
import stage
import constants
import time
import random
# function for the splash scene
def splash_scene():
    # sounds
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")


    background = stage.Grid(image_bank_mt_background,constants.SCREEN_X, constants.SCREEN_Y)

    background.tile(2, 2, 0)  # blank white

    background.tile(3, 2, 1)

    background.tile(4, 2, 2)

    background.tile(5, 2, 3)

    background.tile(6, 2, 4)

    background.tile(7, 2, 0)  # blank white


    background.tile(2, 3, 0)  # blank white

    background.tile(3, 3, 5)

    background.tile(4, 3, 6)

    background.tile(5, 3, 7)

    background.tile(6, 3, 8)

    background.tile(7, 3, 0)  # blank white


    background.tile(2, 4, 0)  # blank white

    background.tile(3, 4, 9)

    background.tile(4, 4, 10)

    background.tile(5, 4, 11)

    background.tile(6, 4, 12)

    background.tile(7, 4, 0)  # blank white


    background.tile(2, 5, 0)  # blank white

    background.tile(3, 5, 0)

    background.tile(4, 5, 13)

    background.tile(5, 5, 14)

    background.tile(6, 5, 0)

    background.tile(7, 5, 0)  # blank white

    #background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_X)

    game = stage.Stage(ugame.display, constants.FPS)

    game.layers = [background]

    game.render_block()

    while True: 
        # Wait for 2 seconds
        time.sleep(2.0)
        menu_scene()



        

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
    # creates a random background everytime we start the game 
    for x_location in range (constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)
    # Sprites
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    alien = stage.Sprite(image_bank_sprites, 9, int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2), 16)
    # list for the lasers for when we shoot
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)
    # refresh rate to 60 fps 
    game = stage.Stage(ugame.display, constants.FPS)
    # Set the images that will show up
    game.layers = lasers + [ship] + [alien] + [background]
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
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break
                
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)

                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        # Redraw Sprite
        game.render_sprites(lasers + [ship] + [alien])
        game.tick()

        
if __name__ == "__main__":
    menu_scene()