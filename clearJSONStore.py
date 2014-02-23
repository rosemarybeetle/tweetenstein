# clearJSONStore.py

def clearJSON ():
    tweets = open('tweetstore.json', 'w') # overwrite existing file
    tweets.write('')
    tweets.close()
