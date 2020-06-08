import pygame

from General import EasyMode, Mouse


class MainGUI:

    def __init__(self, **kwargs):

        self.screen = kwargs.get("screen")
        self.display_width, self.display_height = pygame.display.get_surface().get_size()

        self.mouse = kwargs.get("mouse")

        self.gui_option_dict = {
            "Take Test": None,
            "View Statistics": None
        }
        self.menu_button_list = self.get_menu_button_list()

        self.setup_screen()

    def get_menu_button_list(self):
        menu_button_list = []
        for gui_option in self.gui_option_dict:
            menu_button_list.append(

            )
        return menu_button_list

    def setup_screen(self):

        rect_list = []
        for gui_option in self.gui_option_dict:
            rect_list.append(
                EasyMode.EasyRect(

                )
            )

    def update_parameters(self):
        self.display_width, self.display_height = pygame.display.get_surface().get_size()
        self.mouse.update()

    def run(self):

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
                        # self.run_to_csv()
                        pygame.quit()


def test():

    pygame.init()
    pygame.font.init()
    display_height = 700
    display_width = 1200
    screen = pygame.display.set_mode([display_width, display_height], pygame.RESIZABLE)
    mouse = Mouse.Mouse()

    gui_test = MainGUI(
        screen=screen,
        display_width=display_width,
        display_height=display_height,
        mouse=mouse
    )
    gui_test.run()
