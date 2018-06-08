import praw
import re
import urllib.request
import ctypes
import os

#Setup crawler (?)
reddit = praw.Reddit(client_id='tsGiwf_J6M00XQ',
                                 client_secret='kJBYx6ep7tep-H8Qr7bCDXaxsSU',
                                 password='Eminemboy46',
                                 user_agent='com.hotbackground.bot',
                                 username='YourHomicidalApe')

#Find the top 5 'hot' posts on r/EarthPorn
earthporn = reddit.subreddit('EarthPorn').hot(limit=5)

newPost = False;

#image_path = "C:\\Users\\mwkba\\Desktop\\Programs\\Python\\$EXPORTED\\Wallpaper\\Background.png";
image_path = os.getcwd() + "\\Background.png";

bestRatio = -1000000
bestUrl = ""

#Scan the list
for i in earthporn:
        #Make sure it's not imgur or flickr (there's probably a more elequant way to do this)
        if i.url[0:16] != "http://imgur.com" and i.url[0:17] != "https://imgur.com":
                if i.stickied == False:
                        if i.url[0:22] != "https://www.flickr.com" and i.url[0:21] != "http://www.flickr.com":
                                #Find the text inside of the bracket or parantheses
                                if i.title.find("[") != -1 and i.title.find("]") != -1:
                                        dimensions = i.title[i.title.find("[")+1:i.title.find("]")];
                                        if(dimensions == 'OC'):
                                                first = i.title.find("]")
                                                if i.title.find("[",first) != -1 and i.title.find("]",first+1) != -1:
                                                        dimensions = i.title[i.title.find("[",first)+1:i.title.find("]",first+1)]

                                        if(dimensions.find("x") != -1):
                                                ratio = float(dimensions[:dimensions.find("x")]) / float(dimensions[dimensions.find("x")+1:]);
                                                if(abs(1.6 - ratio) < abs(1.6 - bestRatio)):
                                                        bestUrl = i.url;
                                                        bestRatio = ratio;

os.remove(image_path)
urllib.request.urlretrieve(bestUrl, image_path)

#Set the background to the local\Pictures\Background.png
ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
