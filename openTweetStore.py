# retrieveTweetsStoreContents
import json
def retrieveTweetStore ():
    savedTweets = open('tweetstore2.json', 'r')
    cons = savedTweets.read()
    tweets = json.loads(cons)
    x=0
    l=0
    global hh
    while x<150: # not dynamic, but x can never be more than 100 anyway due to twitter api rate cappining
        try:
            hh=tweets['store'][x]['tweet_id']
            print ('hh = '+hh)
            x=x+1
        except:
            l=x
            print ('length = '+str(l))
            break
    x=0
    l=x
    while x<150: # not dynamic, but x can never be more than 100 anyway due to twitter api rate cappining
        try:
            hh=tweets['store'][x]['tweet_text']
            print ('tweet['+str(x)+'] = '+hh)
            yy=hh.split(' ')
            
            print (yy)
            print('#########')
            x=x+1
        except:
            l=x
            print ('returned '+str(l)+' tweets')
            break
    print ('-------------')
    print ('-------------')
   
    #print('cons = '+cons)

    print ('-------------')
    #print (tweets)
   
    
    print ('-------------')
    savedTweets.close()
retrieveTweetStore()

