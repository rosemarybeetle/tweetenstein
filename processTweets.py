# processTweets.py
# this file defines the post-harvesting text processing that takes the last n tweets and creates the text pools for the visualisor

import json # will be needed to handle json


def processTweets ():
    
    contents = open('tweetstore2.json', 'r')
    cons = contents.read()
    ct = json.loads(cons)
    print (ct['store'])
    x=0
    
    vv=ct['store'][5]['username']
    print(str(vv))
    print 
    contents.close()
processTweets()
