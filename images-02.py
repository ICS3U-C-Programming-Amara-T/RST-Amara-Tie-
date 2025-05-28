#!/usr/bin/env python3
# Created by: Amara Tie 
# Date: May 28, 2025
# This program displays our opening message

import ugame
import stage 

def game_scene():
    print("\n")
    print("Welcome to Cupid's \n ")
    print("Matchmaking game!")

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)

    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()
    
# Gaming Loop
    while True:
        pass

if __name__== "__main__":
    game_scene()