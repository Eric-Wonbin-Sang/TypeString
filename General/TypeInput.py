import pygame
import datetime

from General import EasyMode


class TypeInput:

    def __init__(self, **kwargs):

        self.target_word = kwargs.get("target_word")
        self.display_width = kwargs.get("display_width")
        self.display_height = kwargs.get("display_height")
        self.curr_key_list = []
        self.time_info_dict_list = []

        self.input_text = self.get_input_text()
        self.target_word_text = self.get_target_word_text()

        self.key_dict = {
            pygame.K_LCTRL: "ctrl",
            pygame.K_RCTRL: "ctrl",
            pygame.K_RETURN: "enter",
            pygame.K_BACKSPACE: "backspace",
            pygame.K_DELETE: "delete",
            pygame.K_CAPSLOCK: "capslock",
            pygame.K_LSHIFT: "shift",
            pygame.K_RSHIFT: "shift",
            pygame.K_ESCAPE: "escape"
        }

        self.good_color = (0, 255, 0)
        self.bad_color = (255, 0, 0)
        self.text_line = None

    def get_input_text(self):
        return EasyMode.EasyText(
            text="",
            x=self.display_height / 2 + 100,
            y=self.display_width / 2,
            size=self.display_height / 20,
            font_file="FontFolder/Product Sans Regular.ttf",
            color=(9, 44, 99),
            opacity=100,
            draw_center=True
        )

    def get_target_word_text(self):
        return EasyMode.EasyText(
            text=self.target_word.text,
            x=self.display_height / 2 - 80,
            y=self.display_width / 2,
            size=self.display_height / 20,
            font_file="FontFolder/Product Sans Regular.ttf",
            color=(9, 44, 99),
            opacity=100,
            draw_center=True
        )

    def get_background_rect(self):
        return EasyMode.EasyRect(
            x=self.display_height/2,
            y=self.display_width/2,
            width=self.display_width/3,
            height=self.display_height/10,
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
        ret_str = "{} check - {}"
        if self.target_word.text == self.input_text.text:
            print(ret_str.format(self.input_text.text, "correct"))
            return "correct"
        else:
            print(ret_str.format(self.input_text.text, "incorrect"))
            return "incorrect"

    def is_correct_so_far(self):
        if self.input_text.text == self.target_word.text[:len(self.input_text.text)]:
            return True
        return False

    def get_location_data(self):
        return "x: {} y: {}".format(self.background_rect.x, self.background_rect.y)

    def update(self, event):

        key_str = self.key_dict.get(event.key, chr(event.key))

        if event.type == pygame.KEYDOWN:
            self.curr_key_list.append(key_str)
            if self.curr_key_list[-2:] == ['ctrl', 'backspace']:
                self.input_text.text = ""
            elif key_str == "backspace":
                self.input_text.text = self.input_text.text[:-1]
            elif key_str in "1234567890qwertyuiopasdfghjklzxcvbnm[]\\=;',./":
                if "shift" in self.curr_key_list and "capslock" not in self.curr_key_list \
                        or "shift" not in self.curr_key_list and "capslock" in self.curr_key_list:
                    self.input_text.text += key_str.upper()
                else:
                    self.input_text.text += key_str

        elif event.type == pygame.KEYUP:
            if key_str in self.curr_key_list:           # look into this error
                self.curr_key_list.remove(key_str)

        if self.input_text.text == "":
            self.background_rect.color = self.background_rect.default_color
        else:
            self.background_rect.color = self.good_color if self.is_correct_so_far() else self.bad_color

        self.time_info_dict_list.append(
            {
                "time": datetime.datetime.now(),
                "current_word": self.target_word.text,
                "key_type": "up" if event.type == pygame.KEYUP else "down",
                "key_str": key_str,
                "curr_key_list": self.curr_key_list,
                "curr_input": self.input_text.text
            }
        )

        str_ret = ""
        for key in self.time_info_dict_list[-1]:
            str_ret += "{}\t: {}\t".format(key, self.time_info_dict_list[-1][key])
        print(str_ret)

    def end_check(self):
        self.background_rect.color = self.good_color if self.input_text.text == self.target_word.text else self.bad_color

    def is_mouse_clicked(self, mouse):
        return self.background_rect.is_mouse_clicked(mouse)

    def draw(self, screen):

        self.target_word_text.x = self.background_rect.x - self.background_rect.width/4
        self.input_text.x = self.background_rect.x + self.background_rect.width/4

        self.target_word_text.y = self.background_rect.y
        self.input_text.y = self.background_rect.y

        self.background_rect.draw(screen)
        self.target_word_text.draw(screen)
        self.input_text.draw(screen)
