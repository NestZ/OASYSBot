from twython import Twython
import requests
import datetime

#API end-point
URL = "https://www.cmuccdc.org/api/dustboy/value/6/avghr/all?format=json"

#SetApiKey:
TWITTER_APP_KEY = 'QGjQsgP88D3nPT1DMpns8dSYI'
TWITTER_APP_KEY_SECRET = 'T6GEHds8fXFLGVRN8TEz3VVjG6MkoIjVF8ReGKbqd9mtU4qX5S'
TWITTER_ACCESS_TOKEN = '1050645968914268161-oZHDZkHxpt0r8X10Nydv49RIBdetaj'
TWITTER_ACCESS_TOKEN_SECRET = 'EoIIReylrKCezD78q1o8jl9wTXW23IPLmc1pcvXXAAn4b'

#CreateObj:
twitter = Twython(app_key=TWITTER_APP_KEY,
            	  	  app_secret=TWITTER_APP_KEY_SECRET,
            	  	  oauth_token=TWITTER_ACCESS_TOKEN,
            	  	  oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

#GetJSON:
JSONData = requests.get(url = URL).json()

#LoadData:
pm25Data = JSONData[0]["value"][0]["pm25"]
pm10Data = JSONData[0]["value"][0]["pm10"]
#dateData = JSONData[0]["value"][0]["log_datetime"]
nameData = JSONData[0]["dustboy_name"]

#GetTime
time = datetime.datetime.now()

#assignString:
DATE = 'Date : ' + time.strftime("%d") + '/' + time.strftime("%m") + '/' + time.strftime("%Y")
TIME = 'Time : ' + time.strftime("%H") + ':' + time.strftime("%M") + ':' + time.strftime("%S")
PM10 = 'PM 10 : ' + pm10Data
PM25 = 'PM 2.5 : ' + pm25Data
STATIONNAME = 'Station : ' + nameData

#LoadPic:
photo = open('./img/logo.png', 'rb')
response = twitter.upload_media(media=photo)

#Tweet:
Status = DATE + '\n' + TIME + '\n' + STATIONNAME + '\n' + PM10 + '\n' + PM25 + '\n'
twitter.update_status(status=Status, media_ids=[response['media_id']])
