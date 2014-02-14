# saveTweetsCSV.py

def saveTweet (tw):
    tweets = open('tweetstore.CSV', 'a')
    tweets.write(tw)
    tweets.write('\n')
    tweets.close()
