import time
import board
# import digitalio # For use with SPI
import busio
import adafruit_bmp280

# Create library object using our Bus I2C port
i2c = busio.I2C(board.IO40, board.IO41)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, 0x76)

# change this to match the location's pressure (hPa) at sea level
bmp280.sea_level_pressure = 1013.25

while True:
    print("\nTemperature: %0.1f C" % bmp280.temperature)
    print("Pressure: %0.1f hPa" % bmp280.pressure)
    print("Altitude = %0.2f meters" % bmp280.altitude)
    time.sleep(2)
