import pyglet
from pyglet.window import key

from DIPPID import SensorUDP
from segment import Segment
from utils import WINDOW_WIDTH, WINDOW_HEIGHT

PORT = 5700
TILT_THRESHOLD = 0.5

sensor = SensorUDP(PORT)

# Game class for managing the game and controls

class Game:

    def __init__(self):
        self.game_over = False
        self.has_started = False
        self.won = False
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

    def handle_tilt(self, data):
        if sensor.has_capability('accelerometer'):
            x_tilt = sensor.get_value('accelerometer')['x']
            y_tilt = sensor.get_value('accelerometer')['y']

            if x_tilt < -TILT_THRESHOLD:
                self.factor = -1
                self.direction = 'x'
            if x_tilt > TILT_THRESHOLD:
                self.factor = 1
                self.direction = 'x'
            if y_tilt < -TILT_THRESHOLD:
                self.factor = -1
                self.direction = 'y'
            if y_tilt > TILT_THRESHOLD:
                self.factor = 1
                self.direction = 'y'

    def handle_button_press(self, data):
        if not self.has_started:
            self.has_started = True
        if self.game_over or self.won:
            self.reset_game()

    def reset_game(self):
        self.segments = [Segment(400, 400, (255, 0, 0))]
        self.game_over = False
        self.won = False
        self.score = 0

    def draw_start_game_screen(self):
        pyglet.text.Label('Welcome to Snake', font_name='Courier New', font_size=36, x=WINDOW_WIDTH//2, y=WINDOW_HEIGHT//2 + 40, anchor_x='center', anchor_y='center').draw()
        pyglet.text.Label('Press any button to start', font_name='Courier New', font_size=20, x=WINDOW_WIDTH//2, y=WINDOW_HEIGHT//2 - 40, anchor_x='center', anchor_y='center').draw()

    def draw_game_over_screen(self):
        pyglet.text.Label('GAME OVER', font_name='Courier New', font_size=36, x=WINDOW_WIDTH//2, y=WINDOW_HEIGHT//2 + 40, anchor_x='center', anchor_y='center').draw()
        pyglet.text.Label(f'Your Score: {self.score}', font_name='Courier New', font_size=20, x=WINDOW_WIDTH//2, y=WINDOW_HEIGHT//2, anchor_x='center', anchor_y='center').draw()
        pyglet.text.Label('Press any button to restart', font_name='Courier New', font_size=20, x=WINDOW_WIDTH//2, y=WINDOW_HEIGHT//2 - 40, anchor_x='center', anchor_y='center').draw()

    def draw_winning_screen(self):
        pyglet.text.Label('YOU WON!', font_name='Courier New', font_size=36, x=WINDOW_WIDTH//2, y=WINDOW_HEIGHT//2 + 40, anchor_x='center', anchor_y='center').draw()
        pyglet.text.Label(f'Your Score: {self.score}', font_name='Courier New', font_size=20, x=WINDOW_WIDTH//2, y=WINDOW_HEIGHT//2, anchor_x='center', anchor_y='center').draw()
        pyglet.text.Label('Press any button to restart', font_name='Courier New', font_size=20, x=WINDOW_WIDTH//2, y=WINDOW_HEIGHT//2 - 40, anchor_x='center', anchor_y='center').draw()