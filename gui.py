import pygame

import Word
import TypeInput


def do_input_analysis(curr_word, curr_input):
    print(" - ", end="")
    if curr_word.text == curr_input:
        print("correct")
    else:
        print("incorrect")


def gui():

    pygame.init()
    pygame.font.init()
    display_height = 1200
    display_width = 700
    screen = pygame.display.set_mode([display_height, display_width], pygame.RESIZABLE)

    word_list = Word.get_word_list()
    left_hand_word_list = Word.get_left_hand_word_list(word_list)
    right_hand_word_list = Word.get_right_hand_word_list(word_list)

    curr_word_list = left_hand_word_list

    type_input_list_index = 0
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

    prev_and_next_count = 3

    prev_type_input_list = type_input_list[(type_input_list_index - prev_and_next_count if type_input_list_index - prev_and_next_count >= 0 else 0):type_input_list_index]
    curr_type_input = type_input_list[type_input_list_index]
    next_type_input_list = type_input_list[type_input_list_index + 1:type_input_list_index + 1 + prev_and_next_count]

    loop_counter = 0
    while True:

        screen.fill((255, 255, 255))
        display_width, display_height = pygame.display.get_surface().get_size()
        type_input_y_offset = display_height / 8


        # print([x.target_word for x in prev_type_input_list])
        # print([x.target_word for x in next_type_input_list])
        # print("-------------------------")

        if loop_counter == 0:
            # for i, type_input in enumerate(prev_type_input_list):
            #     type_input.move(x=display_width / 2 + 40, y=display_height / 2 + type_input_y_offset * -(i + 1))
            curr_type_input.move(x=display_width / 2, y=display_height / 2)
            for i, type_input in enumerate(next_type_input_list):
                type_input.move(x=display_width / 2, y=display_height / 2 + type_input_y_offset * (i + 1))
            print([x.target_word for x in prev_type_input_list])
            print(curr_type_input.target_word)
            print([x.target_word for x in next_type_input_list])
            print("-------------------------")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    type_input_list_index += 1

                    prev_type_input_list = type_input_list[(type_input_list_index - prev_and_next_count if type_input_list_index - prev_and_next_count >= 0 else 0):type_input_list_index]
                    curr_type_input = type_input_list[type_input_list_index]
                    next_type_input_list = type_input_list[type_input_list_index + 1:type_input_list_index + 1 + prev_and_next_count]

                    for i, type_input in enumerate(reversed(prev_type_input_list)):
                        type_input.move(x=display_width / 2, y=display_height / 2 + type_input_y_offset * -(i + 1))
                    curr_type_input.move(x=display_width / 2, y=display_height / 2)
                    for i, type_input in enumerate(next_type_input_list):
                        type_input.move(x=display_width / 2, y=display_height / 2 + type_input_y_offset * (i + 1))

                    print([x.target_word for x in prev_type_input_list])
                    print(curr_type_input.target_word)
                    print([x.target_word for x in next_type_input_list])
                    print("-------------------------")

                else:
                    curr_type_input.update(event=event)

        # ------------------------------------------------------

        for i, type_input in enumerate(prev_type_input_list + [curr_type_input] + next_type_input_list):
            type_input.draw(screen=screen)

        if type_input_list_index >= len(type_input_list):
            type_input_list_index = 0

        pygame.display.flip()
        loop_counter += 1


gui()
