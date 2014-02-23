# processTweets.py
# this file defines the post-harvesting text processing that takes the last n tweets and creates the text pools for the visualisor

import json # will be needed to handle json


def processTweets ():
    
    contents = open('tweetstore2.json', 'r')
    cons = contents.read()
    ct = json.loads(cons)
    #print(max)
    global maxy
    x=0
    while (x<100):
        try:
            gotdata = (ct['store'][x])
            x=x+1
        except IndexError:
            gotdata = 'null'
            maxy=x
            print ('max = '+str(maxy))
            break
         
    y=0
    while (y<maxy):
        un=ct['store'][y]['username']
        print(str(un))
        y=y+1
    y=0
    while (y<maxy):
        tid=ct['store'][y]['tweet_id']
        print(str(tid))
        y=y+1
    y=0
    while (y<maxy):
        sn=ct['store'][y]['screen_name']
        print(str(sn))
        y=y+1
    y=0
    while (y<maxy):
        tt=ct['store'][y]['tweet_text']
        print(str(tt))
        y=y+1
        
    print('-----------------')
         
        
    contents.close()
    
processTweets()
