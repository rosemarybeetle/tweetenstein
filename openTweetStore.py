# retrieveTweetsStoreContents
import json

global le
le = 0
def saveUserMentions (un):
    un=un.replace(":","")
    un=un.replace("...","")
    try :
        usernames = open('mentions.txt', 'a')
        usernames.write(',\"'+un+'\"')
        usernames.close()
    except:
        print ('error oepning mentions.txt')
def saveHashtags (ht):
    ht=ht.replace(":","")
    ht=ht.replace("...","")
    try:
        hashtags = open('hashtags.txt', 'a')
        hashtags.write(',\"'+ht+'\"')
        hashtags.close()
    except:
        print ('error oepning hashtags.txt')


def retrieveTweetStore ():
    savedTweets = open('tweetstore2.json', 'r')
    cons = savedTweets.read()
    tweets = json.loads(cons)
    x=0
    l=0
    #global le
    global hh
    while x<150: # not dynamic, but x can never be more than 100 anyway due to twitter api rate capping
        try:
            hh=tweets['store'][x]['tweet_id']
            print ('hh = '+hh)
            x=x+1
        except:
            l=x
            print ('length = '+str(l))
            break
    x=0
    
    usernames = open('mentions.txt', 'w')
    usernames.write('[')
    usernames.close()
    while x<150: # not dynamic, but x can never be more than 100 anyway due to twitter api rate cappining
        try:
            hh=tweets['store'][x]['tweet_text']
            print ('tweet['+str(x)+'] = '+hh)
            yy=hh.split(' ')
            print (yy)
            global le
            le=len(yy)
            ck=0
            i=0
            while i<le:
                at=yy[i].find('@')
                if at==0:
                    
                    if i<(le-1) and x==0 and ck==0:
                        ck=1
                        print ('BANG')
                        usernames = open('mentions.txt', 'a')
                        oo=yy[i]
                        oo=oo.replace(":","")
                        oo=oo.replace("...","")
                        usernames.write('\"'+oo+'\"')
                        print ('oo= ='+oo)
                        usernames.close()
                    else:
                        saveUserMentions(yy[i])
                        print (yy[i])
                        print ('i = '+str(i))
                        ck=ck+1                   
                i=i+1
            print ('length of yy[] = '+str(le) )
            print('#########')
            x=x+1
        except:
            print (' some thing wrong here...')
            usernames = open('mentions.txt', 'a')
            usernames.write(']')
            usernames.close()
            l=x
            print ('returned '+str(l)+' tweets')
            break
    print ('------------- usernames processed -----------------')
    x=0 # reset counter
    print ('inside hashtags, yy = ')
    print (yy)
    hashtags = open('hashtags.txt', 'w')
    hashtags.write('[')
    hashtags.close()
    while x<150: # not dynamic, but x can never be more than 100 anyway due to twitter api rate cappining
        try:
            hh=tweets['store'][x]['tweet_text']
            print ('tweet['+str(x)+'] = '+hh)
            yy=hh.split(' ')
            print (yy)
            #global le
            le=len(yy)
            ck=0
            i=0
           
            while i<le:
                at=yy[i].find('#')
                if at==0:
                    
                    if i<(le-1) and x==0 and ck==0:
                        ck=1
                        print ('hashtag BANG')
                        hashtags = open('hashtags.txt', 'a')
                        oo=yy[i]
                        oo=oo.replace(":","")
                        oo=oo.replace("...","")
                        hashtags.write('\"'+oo+'\"')
                        print ('oo= ='+oo)
                        hashtags.close()
                    else:
                        saveHashtags(yy[i])
                        print (yy[i])
                        print ('i = '+str(i))
                        ck=ck+1                   
                i=i+1
            print ('length of jj[] = '+str(le) )
            print('#########')
            x=x+1
        except:
            hashtags = open('hashtags.txt', 'a')
            hashtags.write(']')
            hashtags.close()
            l=x
            print ('returned '+str(l)+' tweets')
            break
    print ('------------- hashtags processed -----------------')
    savedTweets.close()
    
retrieveTweetStore()
