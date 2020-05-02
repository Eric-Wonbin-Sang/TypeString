import pygame

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
    left_hand_word_list = Word.order_word_list_by_hand("left", word_list)
    right_hand_word_list = Word.order_word_list_by_hand("right", word_list)

    # print(Word.word_list_to_str(word_list))
    # print(Word.word_list_to_str(left_hand_word_list))
    # print(Word.word_list_to_str(right_hand_word_list))

    word_index = 0
    curr_word = word_list[word_index]
    curr_input = ""

    print("{}: ".format(curr_word.text), end="")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    break
                if event.key == pygame.K_SPACE:

                    do_input_analysis(curr_word, curr_input)

                    curr_input = ""
                    word_index += 1
                    curr_word = word_list[word_index]
                    print("{}: ".format(curr_word.text), end="")

                    break

                curr_input += str(chr(event.key))

                print(str(chr(event.key)), end="")




main()
