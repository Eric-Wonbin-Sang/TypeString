import pygame
from pygame import Rect
import pygame.freetype


class EasyRect(Rect):

    def __init__(self, **kwargs):

        self.x = kwargs.get("x", 0)
        self.y = kwargs.get("y", 0)
        self.width = kwargs.get("width", 0)
        self.height = kwargs.get("height", 0)
        self.color = kwargs.get("color", (0, 0, 0))
        self.border_thickness = kwargs.get("border_thickness", 0)
        self.draw_center = kwargs.get("draw_center", True)

        super().__init__(
            int(self.x),
            int(self.y),
            self.width,
            self.height
        )

    def update_coordinates(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        if self.draw_center:
            pygame.draw.rect(
                screen, self.color,
                (self.x - self.width/2, self.y - self.height/2, self.width, self.height),
                self.border_thickness
            )
        else:
            pygame.draw.rect(
                screen, self.color,
                (self.x, self.y, self.width, self.height),
                self.border_thickness
            )


class EasyText(pygame.freetype.Font):

    def __init__(self, **kwargs):

        self.font_file = kwargs.get("font_file")
        self.size = kwargs.get("size")

        super().__init__(
            self.font_file,
            self.size
        )

        self.text = kwargs.get("text")

        self.x = kwargs.get("x", 0)
        self.y = kwargs.get("y", 0)
        self.color = kwargs.get("color", (0, 0, 0))
        self.opacity = kwargs.get("opacity", 100)
        self.draw_center = kwargs.get("draw_center", True)
        self.draw_from_bottom = kwargs.get("draw_from_bottom", False)

    def update_coordinates(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        text_surface, rect = self.render(self.text, self.color)
        text_surface.set_alpha(self.opacity)

        x_offset = 0
        y_offset = 0

        if self.draw_center:
            screen.blit(text_surface, (self.x + x_offset - rect.width / 2, self.y + y_offset - rect.height + self.size/2))
        else:
            screen.blit(text_surface, (self.x + x_offset, self.y + y_offset))
