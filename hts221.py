import time
import board
import busio
import adafruit_hts221

i2c = busio.I2C(board.IO40, board.IO41)
hts = adafruit_hts221.HTS221(i2c)
while True:
    print("Humidity: %.2f percent rH" % hts.relative_humidity)
    print("Temperature: %.2f C" % hts.temperature)
    time.sleep(1)
