from DIPPID import SensorUDP
PORT = 5700
sensor = SensorUDP(PORT)

def handle_btn(data):
    if data == 1:
        print('button pressed')
    else:
        print('button released')

sensor.register_callback('button_1', handle_btn)