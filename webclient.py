from secrets import secrets
import ipaddress
import ssl
import wifi
import socketpool
import adafruit_requests

# URLs to fetch from
TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"
JSON_QUOTES_URL = "https://www.adafruit.com/api/quotes.php"
JSON_STARS_URL = "https://api.github.com/repos/adafruit/circuitpython"

print("Web Client Test")

# create a secrets.py with content below
# secrets = {
#     'ssid' : 'home_wifi_network',
#     'password' : 'wifi_password',
#     'aio_username' : 'my_adafruit_io_username',
#     'aio_key' : 'my_adafruit_io_key',
#     'timezone' : "America/New_York", # http://worldtimeapi.org/timezones
#     }

# load configuration


wifi.radio.connect(secrets['ssid'], secrets['password'])
print("Connecting to %s" % secrets['ssid'])
print("My IP address is", wifi.radio.ipv4_address)

ipv4 = ipaddress.ip_address("8.8.4.4")
print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

print("Fetching text from", TEXT_URL)
response = requests.get(TEXT_URL)
print("-" * 40)
print(response.text)
print("-" * 40)

print()

print("Fetching and parsing json from", JSON_STARS_URL)
response = requests.get(JSON_STARS_URL)
print("-" * 40)
print("CircuitPython GitHub Stars", response.json()["stargazers_count"])
print("-" * 40)

print("done")
