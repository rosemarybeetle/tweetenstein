# saveTweets.py

def saveTweet (tw):
    tweets = open('tweetstore.json', 'a')
    tweets.write(tw)
    tweets.write('\n')
    tweets.close()
