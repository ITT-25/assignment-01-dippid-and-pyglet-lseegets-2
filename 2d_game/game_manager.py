import pyglet
from pyglet.window import key

from segment import Segment
from utils import WINDOW_WIDTH, WINDOW_HEIGHT

# Game class for managing the game

class Game:

    def __init__(self):
        self.game_over = False
        self.segments = [Segment(400, 400, (255, 0, 0))]
        self.factor = 1
        self.direction = 'x'
        self.score = 0

    def on_key_press(self, symbol, modifiers):
        if symbol == key.A:
            self.factor = -1
            self.direction = 'x'
        if symbol == key.D:
            self.factor = 1
            self.direction = 'x'
        if symbol == key.W:
            self.factor = 1
            self.direction = 'y'
        if symbol == key.S:
            self.factor = -1
            self.direction = 'y'
        if symbol == key.SPACE and self.game_over:
            self.reset_game()

    def reset_game(self):
        self.segments = [Segment(400, 400, (255, 0, 0))]
        self.game_over = False
        self.score = 0

    def draw_game_over_screen(self):
        pyglet.text.Label('GAME OVER', font_name='Courier New', font_size=36, x=WINDOW_WIDTH//2, y=WINDOW_HEIGHT//2 + 40, anchor_x='center', anchor_y='center').draw()
        pyglet.text.Label(f'Your Score: {self.score}', font_name='Courier New', font_size=20, x=WINDOW_WIDTH//2, y=WINDOW_HEIGHT//2, anchor_x='center', anchor_y='center').draw()
        pyglet.text.Label('Press SPACE to restart', font_name='Courier New', font_size=20, x=WINDOW_WIDTH//2, y=WINDOW_HEIGHT//2 - 40, anchor_x='center', anchor_y='center').draw()