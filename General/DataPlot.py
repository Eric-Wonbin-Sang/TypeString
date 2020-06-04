import pygame
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg


class DataPlot:

    def __init__(self, **kwargs):
        self.x = kwargs.get("x")
        self.y = kwargs.get("y")
        self.display_width = kwargs.get("display_width")
        self.display_height = kwargs.get("display_height")

        self.x_list = kwargs.get("x_list")
        self.y_list = kwargs.get("y_list")

        self.surf, (self.width, self.height) = self.plot()

    def plot(self):
        fig = plt.figure(figsize=[9, 3])
        canvas = agg.FigureCanvasAgg(fig)

        fig.clf()
        plt.plot(self.x_list, self.y_list, '-')

        canvas.draw()
        renderer = canvas.get_renderer()

        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()

        return pygame.image.fromstring(raw_data, size, "RGB"), size

    def draw(self, screen):
        screen.blit(
            self.surf,
            (int(self.x - self.width / 2), int(self.y - self.height / 2 - self.display_height / 5))
        )
