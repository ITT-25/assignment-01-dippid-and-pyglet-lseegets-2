import pyglet
from pyglet import window, shapes, clock
from pyglet.window import key
import random

from segment import Segment

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SEGMENT_WIDTH = 15
BUFFER = 60

factor = 1
direction = 'x'

win = window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)
segments = []

head = Segment(400, 400, (255, 0, 0))
fruit = shapes.Rectangle(200, 200, SEGMENT_WIDTH, SEGMENT_WIDTH, (255, 255, 0))

def move_fruit():
    fruit.x = random.randint(0, WINDOW_WIDTH - BUFFER)
    fruit.y = random.randint(0, WINDOW_HEIGHT - BUFFER)

def add_segment():
    if len(segments) > 0:
        x = segments[len(segments)-1].prev_x
        y = segments[len(segments)-1].prev_y
    else:
        x = head.prev_x
        y = head.prev_y
    segments.append(Segment(x, y))

def move():
    if direction == 'x':
        head.update_position(head.shape.x + SEGMENT_WIDTH  * factor, head.shape.y)
    elif direction == 'y':
        head.update_position(head.shape.x, head.shape.y + SEGMENT_WIDTH  * factor)

    if len(segments) > 0:
        segments[0].update_position(head.prev_x, head.prev_y)
        for i in range(1, len(segments)):
            segments[i].update_position(segments[i-1].prev_x, segments[i-1].prev_y)

def check_collision():
    if (head.shape.x <  fruit.x + fruit.width and
        head.shape.x + head.shape.width >  fruit.x and
        head.shape.y <  fruit.y + fruit.height and
        head.shape.y + head.shape.height > fruit.y):
        move_fruit()
        add_segment()

def update(dt):
    move()
    check_collision()

@win.event
def on_key_press(symbol, modifiers):
    global factor
    global direction
    if symbol == key.A:
        factor = -1
        direction = 'x'
    if symbol == key.D:
        factor = 1
        direction = 'x'
    if symbol == key.W:
        factor = 1
        direction = 'y'
    if symbol == key.S:
        factor = -1
        direction = 'y'

clock.schedule_interval(update, 0.1)

@win.event
def on_draw():
    win.clear()
    head.shape.draw()
    fruit.draw()
    for i in range(0, len(segments)):
        segments[i].shape.draw()

pyglet.app.run()