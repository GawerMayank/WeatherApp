import requests
import json
import os

city = input ("Enter the city name: ")
url = f"http://api.weatherapi.com/v1/current.json?key=85d4f08609c3420a88642424231711&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
print(w)
os.system(f"say 'The temperature in {city} is {w} degree celsius'")
