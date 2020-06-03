import pygame
import datetime

from General import EasyMode, Functions


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
            opacity=100,
            draw_center=False
        )

    def get_target_word_text(self):
        return EasyMode.EasyText(
            text=self.target_word.text,
            x=self.display_height / 2 - 80,
            y=self.display_width / 2,
            size=self.display_width / 20,
            font_file="FontFolder/Product Sans Regular.ttf",
            color=(9, 44, 99),
            opacity=100,
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
        ret_str = "{} check - {}"
        if self.target_word.text == self.input_text.text:
            self.background_rect.color = (0, 255, 0)
            print(ret_str.format(self.input_text.text, "correct"))
            return "correct"
        else:
            self.background_rect.color = (255, 0, 0)
            print(ret_str.format(self.input_text.text, "incorrect"))
            return "incorrect"

    def is_correct_so_far(self):
        if self.input_text.text == self.target_word.text[:len(self.input_text.text)]:
            return True
        return False

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
            self.curr_key_list.remove(key_str)

        if self.input_text.text == "":
            self.background_rect.color = self.background_rect.default_color
        else:
            if self.is_correct_so_far():
                self.background_rect.color = (0, 255, 0)
            else:
                self.background_rect.color = (255, 0, 0)

        self.time_info_dict_list.append(
            {
                "time": datetime.datetime.now(),
                "key_type": "up" if event.type == pygame.KEYUP else "down",
                "key_str": key_str,
                "curr_key_list": self.curr_key_list
            }
        )

        str_ret = ""
        for key in self.time_info_dict_list[-1]:
            str_ret += "{}\t: {}\t".format(key, self.time_info_dict_list[-1][key])
        print(str_ret)

    # def update_by_curr_input(self, curr_input):
    #
    #     self.input_text.text = curr_input
    #
    #     if self.input_text.text == "":
    #         self.background_rect.color = self.background_rect.default_color
    #     else:
    #         if self.is_correct_so_far():
    #             self.background_rect.color = (0, 255, 0)
    #         else:
    #             self.background_rect.color = (255, 0, 0)

    def draw(self, screen):
        self.background_rect.draw(screen)
        self.target_word_text.draw(screen)
        self.input_text.draw(screen)
