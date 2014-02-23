# clearJSONStore.py

def clearJSON ():
    tweets = open('tweetstore2.json', 'w') # overwrite existing file
    tweets.write('')
    tweets.close()
