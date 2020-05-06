from General import EasyMode


class TypeInput:

    def __init__(self, **kwargs):

        self.display_width = kwargs.get("display_width")
        self.display_height = kwargs.get("display_height")

        self.input_str = kwargs.get("display_width")
        self.target_word = kwargs.get("display_width")

        self.input_text = self.get_input_text()
        self.target_word_text = self.get_target_word_text()

        self.background = self.get_background_rect()
        self.text_line = None

    def get_input_text(self):
        return EasyMode.EasyText(
            text="",
            x=self.display_height / 2,
            y=self.display_width / 2,
            size=self.display_width / 20,
            font_file="FontFolder/Product Sans Regular.ttf",
            color=(9, 44, 99),
            opacity=20,
            draw_center=False
        )

    def get_target_word_text(self):
        return EasyMode.EasyText(
            text=self.target_word.text,
            x=self.display_height / 2,
            y=self.display_width / 2,
            size=self.display_width / 20,
            font_file="FontFolder/Product Sans Regular.ttf",
            color=(9, 44, 99),
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
