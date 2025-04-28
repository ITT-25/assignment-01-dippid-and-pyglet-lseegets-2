from pyglet import shapes

# Segment class representing one segment of the snake

class Segment:

    def __init__(self, x, y, color=(0, 255, 0)):
        self.prev_x = x
        self.prev_y = y
        self.shape = shapes.Rectangle(x, y, 15, 15, color)

    def update_position(self, x, y):
        self.prev_x = self.shape.x
        self.prev_y = self.shape.y
        self.shape.x = x
        self.shape.y = y