import re
# import urllib.request

try: #python3
    from urllib.request import urlopen
except: #python2
    from urllib2 import urlopen

city = raw_input("Please Enter your city: ")

url = "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
data = urlopen(url).read()
data1 = data.decode("utf-8")
print(data1)
