import pyglet
from pyglet import window, shapes, clock
import random

from segment import Segment
from game_manager import Game, sensor
from utils import WINDOW_WIDTH, WINDOW_HEIGHT, OBJ_WIDTH, SEGMENT_WIDTH, BUFFER

# Initialize Game

win = window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)
game = Game()
fruit = shapes.Rectangle(random.randint(0, WINDOW_WIDTH - BUFFER), random.randint(0, WINDOW_HEIGHT - BUFFER), SEGMENT_WIDTH, SEGMENT_WIDTH, (255, 255, 0))


# Move the fruit to a random position. Providing an interval for randrange ensures the fruit stays on the grid

def move_fruit():
    fruit.x = random.randrange(BUFFER, WINDOW_WIDTH - BUFFER, OBJ_WIDTH)
    fruit.y = random.randrange(BUFFER, WINDOW_HEIGHT - BUFFER, OBJ_WIDTH)


# Add a new segment to the snake. Set the last segment's previous position as position for the new segment

def add_segment():
    head = game.segments[0]
    if len(game.segments) > 1:
        x = game.segments[len(game.segments)-1].prev_x
        y = game.segments[len(game.segments)-1].prev_y
    else:
        x = head.prev_x
        y = head.prev_y
    game.segments.append(Segment(x, y))

    if len(game.segments) == (WINDOW_WIDTH - BUFFER) // OBJ_WIDTH:
        game.won = True

# Move the entire snake: Move the head a set distance. Set each subsequent segment's position to the previous position of
# the previous segment

def move():
    head = game.segments[0]
    if game.direction == 'x':
        head.update_position(head.shape.x + OBJ_WIDTH * game.factor, head.shape.y)
    elif game.direction == 'y':
        head.update_position(head.shape.x, head.shape.y + OBJ_WIDTH  * game.factor)

    if len(game.segments) > 1:
        game.segments[1].update_position(head.prev_x, head.prev_y)
        for i in range(2, len(game.segments)):
            game.segments[i].update_position(game.segments[i-1].prev_x, game.segments[i-1].prev_y)


# Check for collisions. If the snake collides with itself or the border, set game_over = True. If the snake collides with
# a fruit, add a new segment, move the fruit and increase the score

def check_collision():
    head = game.segments[0]
    if (head.shape.x < fruit.x + fruit.width and
        head.shape.x + head.shape.width >  fruit.x and
        head.shape.y < fruit.y + fruit.height and
        head.shape.y + head.shape.height > fruit.y):
        move_fruit()
        game.score += 10
        add_segment()
    
    if (head.shape.x <= 0 or head.shape.x + OBJ_WIDTH >= WINDOW_WIDTH or
        head.shape.y <= 0 or head.shape.y + OBJ_WIDTH >= WINDOW_HEIGHT):
        game.game_over = True

    for segment in game.segments[2:]:
        if (head.shape.x < segment.shape.x + segment.shape.width and
            head.shape.x + head.shape.width > segment.shape.x and
            head.shape.y < segment.shape.y + segment.shape.height and
            head.shape.y + head.shape.height > segment.shape.y):
            game.game_over = True

def update(dt):
    if not game.game_over and not game.won:
        move()
        check_collision()

clock.schedule_interval(update, 0.1)

@win.event
def on_key_press(symbol, modifiers):
    game.on_key_press(symbol, modifiers)

@win.event
def on_draw():
    win.clear()

    if not game.has_started:
        game.draw_start_game_screen()
    else:
        if game.game_over:
            game.draw_game_over_screen()
        elif game.won:
            game.draw_winning_screen()
        else:
            pyglet.text.Label(f'Score: {game.score}', font_name='Courier New', font_size=20, x=WINDOW_WIDTH-80, y=WINDOW_HEIGHT-30, anchor_x='center').draw()
            fruit.draw()
            for segment in game.segments:
                segment.shape.draw()

sensor.register_callback('accelerometer', game.handle_tilt)
sensor.register_callback('button_1', game.handle_button_press)
sensor.register_callback('button_2', game.handle_button_press)
sensor.register_callback('button_3', game.handle_button_press)

pyglet.app.run()