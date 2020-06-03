from General import EasyMode


class MainGUI:

    def __init__(self, screen):

        self.screen = screen

        self.gui_option_dict = {"Take Test": None,
                                "View Statistics": None}

        self.setup_screen()

    def setup_screen(self):

        # self.x = kwargs.get("x", 0)
        # self.y = kwargs.get("y", 0)
        # self.width = kwargs.get("width", 0)
        # self.height = kwargs.get("height", 0)
        # self.color = kwargs.get("color", (0, 0, 0))
        # self.default_color = self.color
        # self.border_thickness = kwargs.get("border_thickness", 0)
        # self.draw_center = kwargs.get("draw_center", True)

        rect_list = []
        for gui_option in self.gui_option_dict:
            rect_list.append(
                EasyMode.EasyRect(

                )
            )
