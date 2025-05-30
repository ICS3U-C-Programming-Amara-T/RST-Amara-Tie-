#!/usr/bin/env python3
# Created by: Amara Tie 
# Date: May 28, 2025
# This program displays our opening message

import ugame
import stage 

def game_scene():

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)




    image_bank_mt_background = stage.Bank.from.bmp16("mt_game_studio.bmp")

    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, pallete=constants.RED_PALETTE, buffer=None)
    text1.move(40, 110)
    text1.text("PRESS START")
    text.append(text2)

    background = stage.Grid(image_bank_mt_background,constants.SCREEN_X, constants.SCREEN_Y)

    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constnats.SPRITE_SIZE))

    game = stage.Stage(ugame.display, constants.FPS)

    game.layers = text + [background]

    game.render_block()

    background = stage.Grid(image_bank_background, 10, 8)

    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constnats.SPRITE_SIZE))

    game = stage.Stage(ugame.display, 60)

    game.layers = [ship] + [background]

    game.render_block()

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

        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        game.render_sprites([ship] = [alien])
        game.tick()


if __name__== "__main__":
    game_scene()