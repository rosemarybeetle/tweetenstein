# saveLastTweetId.py

def saveTweetId (tweetId):
    tweetIds = open('lastTweet.json', 'w')
    tweetIds.write('{"lasttweetID": "'+tweetId+'"}')
    tweetIds.close()
