from urllib2 import Request, urlopen, URLError
import requests
from pprint import pprint
import json

api_key = '4c6e59c099c05dc723710c8aca8514aa'
user_zip = '21218'
api_call = 'http://api.openweathermap.org/data/2.5/weather?zip=' + user_zip + ',us'
forecast = requests.get(api_call+'&APPID='+api_key)
#pprint(vars(forecast))
forecast = forecast.json()
print(forecast['main']['temp_max'])
print(type(forecast['main']['temp_max']))
