import pygame
import random

import Word

from General import Constants


def do_input_analysis(curr_word, curr_input):

    print(" - ", end="")
    if curr_word.text == curr_input:
        print("correct")
    else:
        print("incorrect")


def main():

    pygame.init()
    pygame.display.set_mode([200, 200])

    # print(Constants.left_hand_key_list)
    # print(Constants.right_hand_key_list)

    word_list = Word.get_word_list()
    left_hand_word_list = [word for word in Word.order_word_list_by_hand("left", word_list) if word.left_hand_key_percent == 100]
    right_hand_word_list = [word for word in Word.order_word_list_by_hand("left", word_list) if word.right_hand_key_percent == 100]

    # print(Word.word_list_to_str(word_list))
    print(Word.word_list_to_str(left_hand_word_list))
    print(Word.word_list_to_str(right_hand_word_list))

    random.shuffle(left_hand_word_list)

    word_index = 0
    curr_word_list = left_hand_word_list
    curr_word = curr_word_list[word_index]
    curr_input = ""

    print("{}: ".format(curr_word.text), end="")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                print(event.key)
                # print("--------------")
                if event.key == pygame.K_SPACE:

                    do_input_analysis(curr_word, curr_input)

                    curr_input = ""
                    word_index += 1
                    curr_word = curr_word_list[word_index]
                    print("{}: ".format(curr_word.text), end="")

                    break

                if event.key == pygame.K_BACKSPACE:
                    if curr_input != "":
                        print(str(chr(event.key)), end="")
                    curr_input = curr_input[:-1]
                else:
                    if chr(event.key).lower() in "qwertyuiopasdfghjklzxcvbnm'":
                        print(str(chr(event.key)), end="")
                        curr_input += str(chr(event.key))

        if word_index == len(curr_word_list) - 1:
            word_index = 0


main()
