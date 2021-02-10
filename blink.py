import time
import board
from digitalio import DigitalInOut, Direction

led = DigitalInOut(board.IO2)
led.direction = Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
