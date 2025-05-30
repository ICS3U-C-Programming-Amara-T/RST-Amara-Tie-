#!/usr/bin/env python3
# Created by: Amara Tie 
# Date: May 28, 2025
# This program displays our opening message

import ugame
import stage 

def game_scene():

    while True: 
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O:
            print("B")
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        if keys & ugame.K_RIGHT:
            ship.move(ship.x, ship.y + 1)
        

if __name__== "__main__":
    game_scene()