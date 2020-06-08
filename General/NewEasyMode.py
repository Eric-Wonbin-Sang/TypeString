
class SimpleRect:

    def __init__(self):
        pass


class SimpleText:

    def __init__(self):
        pass


class EasyRect:

    def __init__(self, **kwargs):

        self.simple_rect = SimpleRect()
        self.simple_text = SimpleText()

        self.top_ratio = kwargs.get("top_ratio")
        self.bottom_ratio = kwargs.get("bottom_ratio")
        self.left_ratio = kwargs.get("left_ratio")
        self.right_ratio = kwargs.get("right_ratio")

    def draw(self, screen):
        pass
