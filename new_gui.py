import pygame
import random

import Word
import TypeInput
from General import EasyMode


def do_input_analysis(curr_word, curr_input):

    print(" - ", end="")
    if curr_word.text == curr_input:
        print("correct")
    else:
        print("incorrect")


def get_left_hand_word_list(word_list, do_shuffle=True):
    left_hand_word_list = [word for word in Word.order_word_list_by_hand("left", word_list) if
                           word.left_hand_key_percent == 100]
    if do_shuffle:
        random.shuffle(left_hand_word_list)
    return left_hand_word_list


def get_right_hand_word_list(word_list, do_shuffle=True):
    right_hand_word_list = [word for word in Word.order_word_list_by_hand("left", word_list) if
                            word.right_hand_key_percent == 100]
    if do_shuffle:
        random.shuffle(right_hand_word_list)
    return right_hand_word_list


def gui():

    pygame.init()
    pygame.font.init()
    display_height = 1200
    display_width = 700
    screen = pygame.display.set_mode([display_height, display_width], pygame.RESIZABLE)

    word_list = Word.get_word_list()
    left_hand_word_list = get_left_hand_word_list(word_list)
    right_hand_word_list = get_right_hand_word_list(word_list)

    curr_word_list = left_hand_word_list

    type_input_list = [
        TypeInput.TypeInput(
            target_word=next_word.text,
            display_width=display_width,
            display_height=display_height,
            x=display_height / 2,
            y=display_width / 2,
            size=display_width / 20,
            font_file="FontFolder/Product Sans Regular.ttf",
            color=(9, 44, 99),
            opacity=20,
            draw_center=False
        )
        for i, next_word in enumerate(curr_word_list)
    ]

    type_input_y_offset = display_height / 8
    for i, type_input in enumerate(type_input_list):
        type_input.move(y_offset=type_input_y_offset * i)

    while True:

        type_input_y_offset = display_height / 8

        screen.fill((255, 255, 255))
        display_width, display_height = pygame.display.get_surface().get_size()

        print(display_width, display_height, type_input_y_offset)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    type_input_list = type_input_list[1:] + [type_input_list[0]]
                    for type_input in type_input_list:
                        type_input.move(y_offset=-type_input_y_offset)
                else:
                    type_input_list[0].update(event=event)

        for type_input in type_input_list:
            type_input.draw(screen=screen)
            type_input.display_width = display_width
            type_input.display_height = display_height

        pygame.display.flip()


gui()
