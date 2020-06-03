import pygame
import random

import Word
import TypeInput


class GUITest:

    def __init__(self, **kwargs):

        self.screen = kwargs.get("screen")
        self.display_width = kwargs.get("display_width")
        self.display_height = kwargs.get("display_height")

        self.word_list = Word.get_word_list()
        self.type_input_list = []

        self.run()

    def run(self):

        curr_type_input = TypeInput.TypeInput(
            target_word=random.choice(self.word_list),
            display_width=self.display_width,
            display_height=self.display_height,
            x=self.display_height / 2,
            y=self.display_width / 2,
            size=self.display_width / 20,
            font_file="FontFolder/Product Sans Regular.ttf",
            color=(9, 44, 99),
            opacity=20,
            draw_center=False
        )

        while True:

            self.display_width, self.display_height = pygame.display.get_surface().get_size()

            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    if event.key == pygame.K_SPACE:
                        pass
                    else:
                        curr_type_input.update(event=event)
            # ------------------------------------------------------

            curr_type_input.draw(screen=self.screen)

            pygame.display.flip()


def test():

    pygame.init()
    pygame.font.init()
    display_height = 1200
    display_width = 700
    screen = pygame.display.set_mode([display_height, display_width], pygame.RESIZABLE)

    gui_test = GUITest(screen=screen, display_width=display_width, display_height=display_height)

    gui_test.run()


test()
