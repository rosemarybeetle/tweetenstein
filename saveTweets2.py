# saveTweets.py

def saveTweet (tw):
    tweets = open('tweetstore2.json', 'a')
    tweets.write(tw)
    tweets.write('\n')
    tweets.close()
