from twython import Twython
import requests

URL = "https://www.cmuccdc.org/api/dustboy/value/6/avghr/all?format=json"

TWITTER_APP_KEY = 'QGjQsgP88D3nPT1DMpns8dSYI'
TWITTER_APP_KEY_SECRET = 'T6GEHds8fXFLGVRN8TEz3VVjG6MkoIjVF8ReGKbqd9mtU4qX5S'
TWITTER_ACCESS_TOKEN = '1050645968914268161-oZHDZkHxpt0r8X10Nydv49RIBdetaj'
TWITTER_ACCESS_TOKEN_SECRET = 'EoIIReylrKCezD78q1o8jl9wTXW23IPLmc1pcvXXAAn4b'

t = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

JSONData = requests.get(url = URL).json()

pm25Data = JSONData[0]["value"][0]["pm25"]
pm10Data = JSONData[0]["value"][0]["pm10"]
dateData = JSONData[0]["value"][0]["log_datetime"]

DATE = 'Date : ' + dateData
PM10 = 'PM 10 : ' + pm10Data
PM25 = 'PM 2.5 : ' + pm25Data

photo = open('./img/logo.png', 'rb')
response = t.upload_media(media=photo)

t.update_status(status=DATE + '\n' + PM10 + '\n' + PM25 + '\n', media_ids=[response['media_id']])
