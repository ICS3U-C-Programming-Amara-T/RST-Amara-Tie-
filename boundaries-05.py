#!/usr/bin/env python3
# Created by: Amara Tie 
# Date: May 28, 2025
# This program displays our opening message

import ugame
import stage
import constants

def game_scene():
    # Background image
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # Sets background size (10 x 8 and 16 x 16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_X)

    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    # Set the frame to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # Set the images that will show up
    game.layers = [ship] + [background]

    # Render background
    game.render_block()

    # Game Loop
    while True: 
        # control keys with boundaries
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

        # Redraw Sprite
        game.render_sprites([ship])
        game.tick()


if __name__== "__main__":
    game_scene()