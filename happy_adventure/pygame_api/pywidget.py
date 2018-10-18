from .pysurface import Canvas

class Widget(Canvas):
    def __init__(master, name, *args, **kwargs):
        self.name = name
        super().__init__(master = master, *args, **kwargs)

    def build(self):
        pass