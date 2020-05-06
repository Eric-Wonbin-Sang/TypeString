import pygame
import random

import Word
from General import EasyMode


def do_input_analysis(curr_word, curr_input):

    print(" - ", end="")
    if curr_word.text == curr_input:
        print("correct")
    else:
        print("incorrect")


def gui():

    display_height = 1200
    display_width = 700

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode([display_height, display_width], pygame.RESIZABLE)
    display_height, display_width = pygame.display.get_surface().get_size()

    word_list = Word.get_word_list()
    left_hand_word_list = [word for word in Word.order_word_list_by_hand("left", word_list) if
                           word.left_hand_key_percent == 100]
    right_hand_word_list = [word for word in Word.order_word_list_by_hand("left", word_list) if
                            word.right_hand_key_percent == 100]

    random.shuffle(left_hand_word_list)
    random.shuffle(right_hand_word_list)

    curr_word_list = right_hand_word_list
    word_index = 0

    input_box = EasyMode.EasyRect(
        x=display_height/2,
        y=display_width/2,
        width=display_height/3,
        height=display_width/10,
        color=(66, 135, 245),
        draw_center=True
    )
    obj_list = [input_box]

    word_text_list = [
        EasyMode.EasyText(
            text=curr_word_list[word_index].text,
            x=display_height / 2,
            y=display_width / 2,
            size=display_width / 20,
            font_file="FontFolder/Product Sans Regular.ttf",
            color=(9, 44, 99),
            opacity=20,
            draw_center=False
        )
    ]

    input_text_list = [
        EasyMode.EasyText(
            text="",
            x=display_height / 2,
            y=display_width / 2,
            size=display_width / 20,
            font_file="FontFolder/Product Sans Regular.ttf",
            color=(227, 52, 108),
            draw_center=False
        )
    ]

    print("{}: ".format(curr_word_list[word_index].text, end=""))
    while True:

        screen.fill((255, 255, 255))
        display_height, display_width = pygame.display.get_surface().get_size()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    do_input_analysis(curr_word_list[word_index], input_text_list[0].text)

                    word_index += 1
                    print("{}: ".format(curr_word_list[word_index].text), end="")
                    word_text_list[0].text = curr_word_list[word_index].text

                    input_text_list = [
                        EasyMode.EasyText(
                            text="",
                            x=display_height / 2,
                            y=display_width / 2,
                            size=display_width / 20,
                            font_file="FontFolder/Product Sans Regular.ttf",
                            color=(227, 52, 108),
                            draw_center=False
                        )
                    ] + input_text_list

                    for input_text in input_text_list[1:]:
                        input_text.y -= 50
                    input_text_list = input_text_list[:6]
                    break

                if event.key == pygame.K_BACKSPACE:
                    if input_text_list[0].text != "":
                        print(str(chr(event.key)), end="")
                    input_text_list[0].text = input_text_list[0].text[:-1]
                else:
                    if chr(event.key).lower() in "qwertyuiopasdfghjklzxcvbnm'":
                        print(str(chr(event.key)), end="")
                        input_text_list[0].text += str(chr(event.key))
                input_text_list[0].text = input_text_list[0].text

                print([x.text for x in input_text_list])

        if input_text_list[0].text == curr_word_list[word_index].text:
            input_text_list[0].color = (28, 252, 3)
        else:
            input_text_list[0].color = (252, 3, 3)

        if word_index == len(curr_word_list) - 1:
            word_index = 0

        for obj in obj_list:
            obj.update_coordinates(display_height / 2, display_width / 2)
        for obj in obj_list:
            obj.draw(screen)
        for word_text in word_text_list:
            word_text.draw(screen)
        for input_text in input_text_list:
            input_text.draw(screen)

        pygame.display.flip()


gui()
