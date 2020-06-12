import pygame
from pygame import Rect


class SimpleObject(Rect):

    def __init__(self, **kwargs):

        self.x = kwargs.get("x", 0)
        self.y = kwargs.get("y", 0)
        self.width = kwargs.get("width", 0)
        self.height = kwargs.get("height", 0)

        self.color = kwargs.get("color", (0, 0, 0))
        self.init_color = self.color
        self.border_thickness = kwargs.get("border_thickness", 0)
        self.draw_center = kwargs.get("draw_center", True)

        super().__init__(
            int(self.x),
            int(self.y),
            self.width,
            self.height
        )


class SimpleRect(SimpleObject):

    def __init__(self):

        super().__init__(
            x=None,
            y=None,
            width=None,
            height=None,
            color=None,
            border_thickness=None,
            draw_center=None
        )


class SimpleText:

    def __init__(self):

        super().__init__(
            x=None,
            y=None,
            width=None,
            height=None,
            color=None,
            border_thickness=None,
            draw_center=None
        )


class EasyRect:

    def __init__(self, **kwargs):

        self.simple_rect = kwargs.get("simple_rect")
        self.simple_text = kwargs.get("simple_text")

        # self.top_ratio = kwargs.get("top_ratio")
        # self.bottom_ratio = kwargs.get("bottom_ratio")
        # self.left_ratio = kwargs.get("left_ratio")
        # self.right_ratio = kwargs.get("right_ratio")

    def draw(self, screen):
        pass


def main():
    easy_rect = EasyRect(
        simple_rect=None,
        simple_text=None,
        top_ratio=None,
        bottom_ratio=None,
        left_ratio=None,
        right_ratio=None
    )


main()
