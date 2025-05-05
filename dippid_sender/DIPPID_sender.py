import socket
import time
import random
import threading
import numpy as np

IP = '127.0.0.1'
PORT = 5700
BTN_INTERVAL = 2
ACCEL_INTERVAL = 0.01

btn_pressed = False
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Simulate button press by alternating between sending 0 and 1 values in random intervals

def press_btn():
    global btn_pressed
    while True:
        if not btn_pressed:
            btn_pressed = True
            btn_value = 1
        else:
            btn_pressed = False
            btn_value = 0

        btn_message = '{"button_1" : ' + str(btn_value) + '}'
        sock.sendto(btn_message.encode(), (IP, PORT))
        time.sleep(random.random() * BTN_INTERVAL)


# Simulate accelerometer data by sending sine/cosine values in short intervals for the x, y, and z axes

def send_accel_data():
    while True:
        for i in range(0, 361):
            acc_x = np.sin(i * np.pi / 180)
            acc_y = -np.sin(i * np.pi / 180)
            acc_z = np.cos(i * np.pi / 180)

            acc_message = '{"accelerometer": {"x": ' + str(acc_x) + ', "y": ' + str(acc_y) + ', "z": ' + str(acc_z) + '}}'
            sock.sendto(acc_message.encode(), (IP, PORT))
            time.sleep(ACCEL_INTERVAL)


# Use threading to run both functions simultaneously

threading.Thread(target=press_btn).start()
threading.Thread(target=send_accel_data).start()