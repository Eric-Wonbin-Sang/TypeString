import pygame
import datetime
import random
import csv

from GUIModes import GUIAnalyse

from General import Functions, TypeInput, Word, Mouse


class GUITest:

    def __init__(self, **kwargs):

        self.screen = kwargs.get("screen")
        self.mouse = kwargs.get("mouse")

        print(self.mouse)

        self.display_width = kwargs.get("display_width")
        self.display_height = kwargs.get("display_height")
        self.type_input_y_offset = self.display_height / 8

        # self.word_list = Word.get_word_list()
        self.word_list = Word.get_left_hand_word_list(Word.get_word_list(), do_shuffle=True)
        self.type_input_list = []

        self.run()

    def get_random_type_input(self):
        return TypeInput.TypeInput(
                            target_word=random.choice(self.word_list),
                            display_width=self.display_width,
                            display_height=self.display_height,
                            x=self.display_width / 2,
                            y=self.display_height / 2,
                            font_file="../FontFolder/Product Sans Regular.ttf",
                            color=(9, 44, 99),
                            opacity=20,
                            draw_center=True
                        )

    def get_init_type_input_list(self, count):
        init_type_input_list = []
        for i in range(count):
            init_type_input_list.append(self.get_random_type_input())
        return init_type_input_list

    def update_parameters(self):
        self.display_width, self.display_height = pygame.display.get_surface().get_size()
        self.type_input_y_offset = self.display_height / 8
        self.mouse.update()

    def position_type_inputs(self, next_type_input_list):
        for i, type_input in enumerate(reversed(self.type_input_list[-10:])):
            type_input.move(x=self.display_width / 2,
                            y=self.display_height / 2 + self.type_input_y_offset * -(i + 1))
        for i, type_input in enumerate(next_type_input_list):
            type_input.move(x=self.display_width / 2,
                            y=self.display_height / 2 + self.type_input_y_offset * i)

    def run(self):

        next_type_input_list = self.get_init_type_input_list(count=4)
        self.position_type_inputs(next_type_input_list=next_type_input_list)
        curr_run_analysis = False
        prev_run_analysis = False

        while True:

            self.update_parameters()
            self.screen.fill((12, 49, 97))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                    if event.key == pygame.K_ESCAPE:
                        self.run_to_csv()
                        pygame.quit()
                    if event.key == pygame.K_SPACE and event.type == pygame.KEYUP:
                        next_type_input_list[0].end_check()
                        self.type_input_list.append(next_type_input_list[0])
                        next_type_input_list = next_type_input_list[1:] + [self.get_random_type_input()]
                        self.position_type_inputs(next_type_input_list=next_type_input_list)
                    else:
                        next_type_input_list[0].update(event=event)

                        if next_type_input_list[0].curr_key_list == ["ctrl", "shift", "a"]:
                            curr_run_analysis = True
                            next_type_input_list[0].curr_key_list = []

            print(next_type_input_list[0].is_mouse_clicked(self.mouse))

            for i, type_input in enumerate(next_type_input_list + self.type_input_list):
                type_input.draw(screen=self.screen)
            pygame.display.flip()

            if curr_run_analysis != prev_run_analysis:
                csv_file_path = "TypeHistory/2020.06.04 20.04 - TypingTest.csv"
                GUIAnalyse.GUIAnalyse(
                    screen=self.screen,
                    display_width=self.display_width,
                    display_height=self.display_height,
                    csv_file_path=csv_file_path
                )

            prev_run_analysis = curr_run_analysis
            curr_run_analysis = False

    def run_to_csv(self):
        directory = "TypeHistory"
        filename = "{} - TypingTest.csv".format(Functions.format_datetime(datetime.datetime.now()))
        with open('{}/{}'.format(directory, filename), 'w', newline='') as csv_file:
            input_csv = csv.writer(csv_file)

            row_count = 0
            for type_input in self.type_input_list:
                for time_info_dict in type_input.time_info_dict_list:
                    if row_count == 0:
                        input_csv.writerow(list(time_info_dict.keys()))
                    input_csv.writerow([str(time_info_dict[key]) for key in time_info_dict])
                    row_count += 1


def test():

    pygame.init()
    pygame.font.init()
    display_height = 700
    display_width = 1200
    screen = pygame.display.set_mode([display_width, display_height], pygame.RESIZABLE)
    mouse = Mouse.Mouse()

    gui_test = GUITest(
        screen=screen,
        display_width=display_width,
        display_height=display_height,
        mouse=mouse
    )
    gui_test.run()


test()
