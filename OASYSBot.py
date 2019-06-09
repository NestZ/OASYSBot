import requests
import datetime
import os
from twython import Twython
from PIL import Image, ImageDraw, ImageFont
from picamera import PiCamera

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
nameData = JSONData[0]["dustboy_name"]

#GetTime
time = datetime.datetime.now()

#assignString:
DATE = 'Date : ' + time.strftime("%d") + '/' + time.strftime("%m") + '/' + time.strftime("%Y")
TIME = 'Time : ' + time.strftime("%H") + ':' + time.strftime("%M") + ':' + time.strftime("%S")
PM10 = 'PM 10 : ' + pm10Data + u' \u03BC' + 'g/' + u'm\u00b3'
PM25 = 'PM 2.5 : ' + pm25Data + u' \u03BC' + 'g/' + u'm\u00b3'
STATIONNAME = 'Station : ' + nameData

#TakePic:
camera = PiCamera()
camera.capture("./img/Picture.jpg")

#MergePic:
Pic = Image.open("./img/Picture.jpg")
Logo = Image.open("./img/logo.jpg")
area = (1600,925,1856,1046)
Pic.paste(Logo, area)
Pic.save('./img/cbpic.png')

#InsertText:
Status = DATE + '\n' + TIME + '\n' + STATIONNAME + '\n' + PM10 + '\n' + PM25 + '\n'
Cbpic = Image.open('./img/cbpic.png')
font_type = ImageFont.truetype('DejaVuSerif.ttf',28)
draw = ImageDraw.Draw(Cbpic)
draw.text(xy=(1275,925),text=Status,fill=(0,0,0),font=font_type)
Cbpic.save('./img/cbpic.png')

#LoadPic:
photo = open('./img/cbpic.png', 'rb')
response = twitter.upload_media(media=photo)

#Tweet:
twitter.update_status(status=Status, media_ids=[response['media_id']])

#Success:
os.remove("./img/Picture.jpg")
os.remove("./img/cbpic.png")
print ("All Complete")
