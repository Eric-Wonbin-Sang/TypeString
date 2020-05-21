import pygame
import datetime

from General import EasyMode, Functions


class TypeInput:

    def __init__(self, **kwargs):

        self.target_word = kwargs.get("target_word")
        self.display_width = kwargs.get("display_width")
        self.display_height = kwargs.get("display_height")
        self.curr_key_list = []
        self.time_key_dict = {}

        self.input_text = self.get_input_text()
        self.target_word_text = self.get_target_word_text()

        self.background_rect = self.get_background_rect()
        self.text_line = None

    def get_input_text(self):
        return EasyMode.EasyText(
            text="",
            x=self.display_height / 2 + 100,
            y=self.display_width / 2,
            size=self.display_width / 20,
            font_file="FontFolder/Product Sans Regular.ttf",
            color=(9, 44, 99),
            opacity=20,
            draw_center=False
        )

    def get_target_word_text(self):
        return EasyMode.EasyText(
            text=self.target_word,
            x=self.display_height / 2 - 80,
            y=self.display_width / 2,
            size=self.display_width / 20,
            font_file="FontFolder/Product Sans Regular.ttf",
            color=(71, 92, 125),
            opacity=20,
            draw_center=False
        )

    def get_background_rect(self):
        return EasyMode.EasyRect(
            x=self.display_height/2,
            y=self.display_width/2,
            width=self.display_height/3,
            height=self.display_width/10,
            color=(66, 135, 245),
            draw_center=True
        )

    def move(self, x=None, y=None, x_offset=0, y_offset=0):

        if x is not None:
            x_offset = x - self.background_rect.x + x_offset
        if y is not None:
            y_offset = y - self.background_rect.y + y_offset

        self.background_rect.x += x_offset
        self.background_rect.y += y_offset

        self.target_word_text.x += x_offset
        self.target_word_text.y += y_offset

        self.input_text.x += x_offset
        self.input_text.y += y_offset

    def do_input_analysis(self):
        print(" - ", end="")
        if self.target_word == self.input_text.text:
            self.background_rect.color = (0, 255, 0)
            print("correct")
        else:
            self.background_rect.color = (255, 0, 0)
            print("incorrect")

    def update(self, event):

        if event.key in [pygame.K_LCTRL, pygame.K_RCTRL]:
            key = "ctrl"
        elif event.key == pygame.K_CAPSLOCK:
            return
        elif event.key == pygame.K_BACKSPACE:
            key = "backspace"
        elif event.key == pygame.K_DELETE:
            key = "delete"
        else:
            key = chr(event.key)

        if event.type == pygame.KEYDOWN:
            self.curr_key_list.append(key)

            if self.curr_key_list[-2:] == ['ctrl', 'backspace']:
                self.input_text.text = ""

            if self.curr_key_list == ["ctrl", "backspace"]:
                self.input_text.text = ""
            elif len(key) == 1 and key in "qwertyuiopasdfghjklzxcvbnm":
                self.input_text.text += key
            elif event.key == pygame.K_BACKSPACE:
                self.input_text.text = self.input_text.text[:-1]

            self.time_key_dict[datetime.datetime.now().time()] = key

        elif event.type == pygame.KEYUP:
            self.curr_key_list.remove(key)

        # print(event.key, chr(event.key), event.type, self.curr_key_list, self.input_text.text)

        print(datetime.datetime.now(), Functions.str_to_length(key, 10), self.input_text.text)

        # for time in self.time_key_dict:
        #     print("\t", time, self.time_key_dict[time])

    def draw(self, screen):
        self.background_rect.draw(screen)
        self.target_word_text.draw(screen)
        self.input_text.draw(screen)
