import tweepy
import requests, json
from dadjokes import Dadjoke

import pushtweet
import pulljoke

import json

with open('credentials.json') as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    # print("Type:", type(data))

    # print("People : ", data["TwitterCredentials"])




joke = pulljoke.generate_joke()

pushtweet.post_tweet(data,joke)