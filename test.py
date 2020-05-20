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

    curr_word_list = left_hand_word_list
    word_index = 0

    # type_input = TypeInput.TypeInput(
    #     display_width=display_width,
    #     display_height=display_height,
    #     target_word=curr_word_list[word_index]
    # )
    type_input_list = [
        TypeInput.TypeInput(
            display_width=display_width,
            display_height=display_height,
            target_word=word
        )
        for word in curr_word_list
    ]
    for i, type_input in enumerate(type_input_list[word_index:]):
        if i == 10:
            break
        type_input.move(y_offset=70 * i)

    print("{}: ".format(curr_word_list[word_index].text, end=""))
    while True:

        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:

                if event.key == pygame.K_SPACE and event.type == pygame.KEYUP:
                    word_index += 1

                    break

                type_input_list[word_index].update(event)

        if word_index == len(curr_word_list) - 1:
            word_index = 0

        for i, type_input in enumerate(type_input_list[word_index:]):
            if i == 10:
                break
            type_input.draw(screen)

        pygame.display.flip()


gui()
