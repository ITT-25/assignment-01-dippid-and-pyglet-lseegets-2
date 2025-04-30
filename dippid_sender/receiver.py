from DIPPID import SensorUDP
from vis import Visualizer

PORT = 5700
sensor = SensorUDP(PORT)
update_frequency = 10


# Visualize accelerometer data (I borrowed the Visualizer from the lecture)

def main():
    visualizer = Visualizer(sensor=sensor, update_freq=update_frequency)   
    visualizer.run()


# Print button status

def handle_btn(data):
    if data == 1:
        print('button pressed')
    else:
        print('button released')


# Print accelerometer data

def handle_acc(data):
    print(data)

sensor.register_callback('button_1', handle_btn)
#sensor.register_callback('accelerometer', handle_acc)

if __name__ == '__main__':
    main()