import json
# Read Cred file for twitter credentials necessary for apis
with open('credentials.json') as json_file:
    data = json.load(json_file)

import time
import tweepy
import requests, json
from dadjokes import Dadjoke

import pushtweet
import pulljoke

import os


# Printing Menu function
def print_menu():
    # Clear console
    clear = lambda: os.system('cls')
    clear()

    # Read menu file
    menu = open('menu.txt', 'r')
    menu_contents = menu.read()

    # Print menu text file contents
    print(menu_contents)

    user_response = input('Your choice from the above options : ')
    return(user_response)



user_decision = print_menu()

if user_decision == '1' :
    joke = pulljoke.generate_joke()
    print('Joke I am about to tweet : ' + joke)
    pushtweet.post_tweet(data,joke)
elif user_decision == '2' :
    print('you want a loop')
    user_mins = input("Fun! How long should I wait (in minutes) before tweeting again?")

    while(True):
        joke = pulljoke.generate_joke()
        print('Joke I am about to tweet : ' + joke)
        pushtweet.post_tweet(data,joke)
        time.sleep(300)

elif user_decision == '3' :
    print('\n\nThank you for using the dad joke twitter bot :)\n\n')