import tweepy

# Create variables for each key, secret, token
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Write a tweet to push to our Twitter account
# 1st Text Only Tweet
tweetText = 'Hello, world!'
api.update_status(status=tweetText)
# 2nd Image Only Tweet
api.update_with_media(filename="helloWorld.jpeg")
# 3rd Both Text and Image
api.update_with_media(filename="helloWorld.jpeg", status=tweetText)
