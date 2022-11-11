import tweepy

all_keys = open("keys.env", "r").read().splitlines()
api_key = all_keys[0]
api_secret = all_keys[1]
access_token = all_keys[2]
access_secret = all_keys[3]

authenticator = tweepy.OAuthHandler(api_key, api_secret)
authenticator.set_access_token(access_token, access_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

api.update_status("My first tweepy tweet!")
