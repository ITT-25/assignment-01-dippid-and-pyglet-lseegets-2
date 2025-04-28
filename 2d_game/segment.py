from pyglet import shapes

class Segment:

    prev_x = 0
    prev_y = 0

    def __init__(self, x, y, color=(0, 255, 0)):
        self.prev_x = x
        self.prev_y = y
        self.shape = shapes.Rectangle(x, y, 15, 15, color)

    def update_position(self, x, y):
        self.prev_x = self.shape.x
        self.prev_y = self.shape.y
        self.shape.x = x
        self.shape.y = y