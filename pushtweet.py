import tweepy

def post_tweet(credentials,tweet):
    print(credentials["TwitterCredentials"][0])

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(credentials["TwitterCredentials"][0]["APIKey"], credentials["TwitterCredentials"][0]["APIKeySecret"])
    auth.set_access_token(credentials["TwitterCredentials"][0]["AccessToken"], credentials["TwitterCredentials"][0]["AccessTokenSecret"])

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    api.update_status(tweet)