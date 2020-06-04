import pygame
import csv


from General import EasyMode, Constants, DataPlot, Functions, WordAttempt


class GUIAnalyse:

    def __init__(self, **kwargs):

        self.screen = kwargs.get("screen")
        self.display_width = kwargs.get("display_width")
        self.display_height = kwargs.get("display_height")

        self.csv_file_path = kwargs.get("csv_file_path")
        self.time_info_dict_list = self.get_time_info_dict_list()
        self.word_attempt_list = self.get_word_attempt_list()
        self.data_plot = self.get_data_plot()

        self.background_rect = self.get_background_rect()

        self.run()

    def get_data_plot(self):

        time_list = [Functions.datetime_str_to_datetime(time_info_dict["time"]) for time_info_dict in
                     self.time_info_dict_list]
        delta_list = []
        for i, time in enumerate(time_list[:-1]):
            delta_list.append((time_list[i + 1] - time).microseconds)

        return DataPlot.DataPlot(
            screen=self.screen,
            x=self.display_width / 2,
            y=self.display_height / 2,
            display_width=self.display_width,
            display_height=self.display_height,
            x_list=time_list[1:],
            y_list=delta_list
        )

    def get_background_rect(self):
        return EasyMode.EasyRect(
            x=self.display_width/2,
            y=self.display_height/2,
            width=self.display_width * .9,
            height=self.display_height * .9,
            color=(8, 32, 64),
            draw_center=True
        )

    def get_time_info_dict_list(self):
        time_info_dict_list = []
        with open("{}/{}".format(Constants.project_directory, self.csv_file_path), newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for info_dict in reader:
                time_info_dict_list.append(info_dict)
        return time_info_dict_list

    def get_word_attempt_list(self):
        prev_current_word = None
        time_info_dict_list_list = []
        dict_list = []
        for i, time_info_dict in enumerate(self.time_info_dict_list):
            curr_current_word = time_info_dict["current_word"]
            if curr_current_word != prev_current_word:
                if dict_list:
                    time_info_dict_list_list.append(dict_list)
                    dict_list = []
            dict_list.append(time_info_dict)
            prev_current_word = curr_current_word
        time_info_dict_list_list.append(dict_list)

        return [
            WordAttempt.WordAttempt(
                time_info_dict_list=time_info_dict_list
            )
            for time_info_dict_list in time_info_dict_list_list
        ]

    def update_dimension_parameters(self):
        self.display_width, self.display_height = pygame.display.get_surface().get_size()

    def analyse(self):

        for word_attempt in self.word_attempt_list:
            print(word_attempt)

        correct_time_info_dict_list_list = []
        incorrect_time_info_dict_list_list = []

        # for time_info_dict_list in self.time_info_dict_list_list:
        #     if time_info_dict_list[-1]["current_word"] == time_info_dict_list[-1]["curr_input"]:
        #         correct_time_info_dict_list_list.append(time_info_dict_list)
        #     else:
        #         incorrect_time_info_dict_list_list.append(time_info_dict_list)
        #
        # for time_info_dict_list in correct_time_info_dict_list_list:
        #     for i, time_info_dict in enumerate(time_info_dict_list):
        #         print(time_info_dict)
        #     print("--------------------")
        #
        # print("\n\n\n")

        # for time_info_dict_list in incorrect_time_info_dict_list_list:
        #     for i, time_info_dict in enumerate(time_info_dict_list):
        #         print(time_info_dict)
        #     print("--------------------")

    def run(self):

        self.analyse()

        run_cond = True
        while run_cond:

            self.update_dimension_parameters()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                    if event.key == pygame.K_ESCAPE:
                        run_cond = False
                        break

            self.background_rect.draw(self.screen)
            self.data_plot.draw(screen=self.screen)

            pygame.display.flip()


def test():

    pygame.init()
    pygame.font.init()
    display_height = 700
    display_width = 1200
    screen = pygame.display.set_mode([display_width, display_height], pygame.RESIZABLE)

    csv_file_path = "TypeHistory/2020.06.03 15.21 - TypingTest.csv"
    GUIAnalyse(
        screen=screen,
        display_width=display_width,
        display_height=display_height,
        csv_file_path=csv_file_path
    )


test()
