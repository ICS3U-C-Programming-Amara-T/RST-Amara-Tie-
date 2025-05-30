#!/usr/bin/env python3
# Created by: Amara Tie 
# Date: May 28, 2025
# This program adds Sprites

import ugame
import stage 

def game_scene():
    # Background image 
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # Sets background size (10 x 8 and 16 x 16)
    background = stage.Grid(image_bank_background, 10, 8)

    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)
    # Set the frame to 60fps
    game = stage.Stage(ugame.display, 60)
    # Set the images that will show up
    game.layers = [ship] + [background]
    # Render background
    game.render_block()
    # Game Loop
    while True:
        # REdraw sprites
        game.render_sprites([ship])
        game.tick()
    
if __name__== "__main__":
    game_scene()
