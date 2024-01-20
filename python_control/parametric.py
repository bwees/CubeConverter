import serial
import time
from python_control.math_functions import *

# Open serial port
ser = serial.Serial('/dev/cu.usbserial-A50285BI', 250000)

ser.write([0]*64)



# convert 3d array of 8x8x8 of Bool to 64 byte array
def send_to_cube(data):
    byteCount = 0
    flatten = [item for sublist in data for item in sublist]

    # flatten is now 64 arrays of 8 bools
    # convert each array to a byte

    byte_array = [0]*64

    for i, arr in enumerate(flatten):
        for j, val in enumerate(arr):
            byte_array[i] += (1 << j) if val else 0


    try:
        for b in byte_array:
            ser.write([b])
            byteCount += 1
    except KeyboardInterrupt:
        ser.write([0]*(64-byteCount))



def sphere_anim(cycles):
    ts = .75
    direction = 1
    count = 0

    while (count < cycles*2):
        ts += .01*direction
        data = [[[in_sphere(x, y, z, 3.5, 3.5, 3.5, ts) for x in range(8)] for y in range(8)] for z in range(8)]
        send_to_cube(data)
        time.sleep(0.001)

        if ts > 4 or ts < .75:
            direction *= -1
            count += 1

def wave_animation(cycles):
    ts = .75
    direction = 1

    for i in range(cycles*625):
        ts += .01*direction
        data = [[[in_wave(x, y, z, 3, 2, ts, 3.5) for x in range(8)] for y in range(8)] for z in range(8)]
        send_to_cube(data)
        time.sleep(0.001)
        
def droplet_animation(cycles):
    ts = .75
    direction = 1

    for i in range(cycles*625):
        ts += .01*direction
        data = [[[in_circular_wave(x, y, z, 3, 2, ts, 3.5) for x in range(8)] for y in range(8)] for z in range(8)]
        send_to_cube(data)
        time.sleep(0.001)

def swapped_droplet_animation(cycles):
    ts = .75
    direction = 1

    for i in range(cycles*625):
        ts += .01*direction
        data = [[[in_swapped_circular_wave(x, y, z, 3, 2, ts, 3.5) for x in range(8)] for y in range(8)] for z in range(8)]
        send_to_cube(data)
        time.sleep(0.001)

direction = 1
while True:
    sphere_anim(5)
    droplet_animation(5)
    wave_animation(5)
    swapped_droplet_animation(5)
