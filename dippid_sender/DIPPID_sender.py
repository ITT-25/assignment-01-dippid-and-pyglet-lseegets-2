import socket
import time
import random

IP = '127.0.0.1'
PORT = 5700

btn_pressed = False

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    if not btn_pressed:
        btn_pressed = True
        btn_value = 1
    else:
        btn_pressed = False
        btn_value = 0

    btn_message = '{"button_1" : ' + str(btn_value) + '}'
    print(btn_message)

    sock.sendto(btn_message.encode(), (IP, PORT))

    time.sleep(random.random() * 10)
