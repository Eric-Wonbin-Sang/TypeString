import pygame

from GUIModes import GUITest


def main():

    pygame.init()
    pygame.font.init()
    display_height = 700
    display_width = 1200
    screen = pygame.display.set_mode([display_width, display_height], pygame.RESIZABLE)

    gui_test = GUITest.GUITest(
        screen=screen,
        display_width=display_width,
        display_height=display_height
    )

    gui_test.run()


main()
