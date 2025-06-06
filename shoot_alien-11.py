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

    # background
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

    # Set the frame to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # Set the images that will show up
    game.layers = [background]
    # Render background
    game.render_block()

    while True: 
        # Wait for 2 seconds
        time.sleep(2.0)
        menu_scene()



        
# main game scene function
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
    text1.move(40, 110)
    text1.text("PRESS START")
    text.append(text2)

    # Sets background size (10 x 8 and 16 x 16)
    background = stage.Grid(image_bank_mt_background,constants.SCREEN_X, constants.SCREEN_Y)
    
    # refresh rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    # Set the images that will show up
    game.layers = text + [background]
    # Render background
    game.render_block()

    while True: 
        # gets the user input
        keys = ugame.buttons.get_pressed()
       
        if keys & ugame.K_START != 0:
            game_scene()
        # redraw sprites
        game.tick()


        
# main game scene function
def game_scene():
    # for the score
    score = 0
    
    def show_alien():   # this function takes an alien from off the screen and moves it onto the screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break
    # images
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # buttons and tehir state
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # sounds
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # Sets background size (10 x 8 and 16 x 16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    # creates a random background everytime we start the game 
    for x_location in range (constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)
    # Sprites 
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    # list for aliens when we shoot
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)
    # places an alien on the screen
    show_alien()
    
    # list for the lasers for when we shoot
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)
    # This is a stage for the background to show up has a refresh rate of 60
    game = stage.Stage(ugame.display, constants.FPS)
    # Set the images that will show up
    game.layers = lasers + [ship] + aliens + [background]
    # Render background
    game.render_block()

    #game loop repeats forever
    while True: 
        # gets the user input
        keys = ugame.buttons.get_pressed()
        # A button pressed states
        if keys & ugame.K_O != 0:
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
        if keys & ugame.K_X != 0:
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
        # each frame moves the lasers that have been fired    
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)

                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        # each frame moves the aliens that are on the screen down 
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)
                # if alien goes off the screen moves off the bottom of the screen put it back to holding area
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_alien()
        # each frame checks if any of the lasers are touching an alien
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:# only looking at laser on screen
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        # stage collision detecter bounding box
                        if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2, lasers[laser_number].x + 11, # these define the bounding box for the laser
                                         lasers[laser_number].y + 12, aliens[alien_number].x + 1, aliens[alien_number].y, # these define the bounding box for the alien
                                         aliens[alien_number].x + 15, aliens[alien_number].y + 15):
                            # when you hit an alien
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)# after hit alien moves off
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)# laser moves off
                            # sound plays
                            boom_sound = open("boom.wav", 'rb')
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            score = score + 1 # 1 point is added to the score
    
        # redraws sprites
        game.render_sprites(lasers + [ship] + aliens)
        game.tick()

        
if __name__ == "__main__":
    menu_scene()