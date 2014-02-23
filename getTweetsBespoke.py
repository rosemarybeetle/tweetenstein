import requests
import saveTweets
import saveTweets2
import clearJSONStore
import clearJSONStore2
import saveLastTweetId
import saveTweetsCSV
import requests_oauthlib
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session
from threading import Timer
import PMRkeys #PMRkeys is a separate local .py file with the Twitter Application Oauth credentials listed (not here for obvious reasons!) 
import json # will be needed to handle json
import sqlite3 as lite # sqlite database
import sys


  
# ---------- define variables -------------------------------
adminURL='https://docs.google.com/spreadsheet/pub?key=0AgTXh43j7oFVdGp1NmxJVXVHcGhIel9CNUxJUk8yYXc&output=csv'
stopwordsURL ='https://docs.google.com/spreadsheet/pub?key=0AgTXh43j7oFVdEJGSWJNRXJJQVc5ZVo2cHNGRFJ3WVE&output=csv'
searchTerm=""
searchType=""
tweetNum=""
harvestPeriod=""
introText=""
text2=""
lastSavedTweetIdDB=0

saveTweet=saveTweets.saveTweet
saveTweet2=saveTweets2.saveTweet
clearJSON=clearJSONStore.clearJSON
clearJSON2=clearJSONStore2.clearJSON
saveTweetCSV=saveTweetsCSV.saveTweet
saveTweetId=saveLastTweetId.saveTweetId

def retrieveTweetIdJS ():
    contents = open('lastTweet.json', 'r')
    cons = contents.read()
    ltids = json.loads(cons)
    global lastSavedTweetIdJS
    lastSavedTweetIdJS=ltids['lasttweetID']
    
    print ('-------------')
    print ('-------------')
   
    print('cons = '+cons)
    print('ID of last tweet saved in JSON file = '+lastSavedTweetIdJS)
    lastSavedTweetIdJS=int(lastSavedTweetIdJS)
    print ('-------------')
    print ('-------------')
    contents.close()
#def jasoniseTweets ():
    
    # turns a line separatedlist of JSON into a full on JSON object


#  --------------------------------------------------------------------------------------
#       ----------- end - above this line are set ups and imports etc ------------
#  --------------------------------------------------------------------------------------


# ------------- search twitter as a function ---------------
def search_tweets (term,count) : # params: term= 'what to search for' type = 'how to search' Count = 'number of tweets' (max 100)    search_url_root='https://api.twitter.com/1.1/search/tweets.json?q='
    retrieveTweetIdJS()
    # check what type the search term is
    clearJSON() # empties the temporary tweet store (line break version)
    clearJSON2() # empties the temporary tweet store (JSON version)
    saveTweet2('[')
    search_url_root='https://api.twitter.com/1.1/search/tweets.json?q='
    x= term.find('#') # look to see what position the hashtag is
    y=term.find('@') # look to see what position the @ sign is
    global termTXT
    if x==0 : #  this is checking if the first character is a hashtag
        print ('searching twitter API for hashtag: '+term)
        term2 = term.split('#')[1] # strip off the hash
        termTXT= term2 # allows the search term to be passed as a parameter
        term='%23'+term2 # add unicode for # sign (%23) if a hashtag search term
    else:
        if y==0: # if @ is the first character
            print ('searching twitter API for username: @'+term)
            term3 = term.split('@')[1] # strip off the @
            termTXT= term3 # allows the search term to be passed as a parameter
            term='%40'+term3 # add unicode for @ sign (%40) if a username search
        else:
            print ('searching for term: '+term) # or just search!
            termTXT= term # allows the search term to be passed as a parameter
    search_url=str(search_url_root+term+'&count='+count) # create the full search url from search term and admin setting for number of results
    print ('---------------------------')
    print ()
    try:
        auth = OAuth1(PMRkeys.PMR_consumer_key, PMRkeys.PMR_consumer_secret,PMRkeys.PMR_access_token,PMRkeys.PMR_access_secret )
        auth_response=requests.get(search_url, auth=auth)
        # print ('auth_response.text') # - uncomment to check the text is returning as expected
        # print (auth_response.text) # - uncomment to check the text is returning as expected
        j = (auth_response.text)
        js = json.loads(j)
        c = int(count)
        x=0
        while (x<c-1):
            try:
                tweet_id = js['statuses'][x]['id']
                testID=int(tweet_id)
                print ('testID= '+str(testID))
                print('-------')
                print ('---------------')
                if (x==0):
                    saveTweetId (str(tweet_id))
                print ('Tweet '+str(x+1)+' of '+str(c)+'. Tweet id: '+str(tweet_id))
                name = js['statuses'][x]['user']['name']
                user = js['statuses'][x]['user']['screen_name']
                username= '@'+user
                print ('From:'+username+'('+name+')')
                tweet = js['statuses'][x]['text']
                # following line gets rid of Twitter line breaks...
                tweet=tweet.replace("\n","")
                tweet=tweet.replace("\"","'")
                
                print (tweet)
                fullTweet='{"tweet_id": "'+str(tweet_id)+'","username": "'+str(username)+'","screen_name": "'+str(name)+'","tweet_text": "'+str(tweet)+'" } '
                fullTweet2='{"tweet_id": "'+str(tweet_id)+'","username": "'+str(username)+'","screen_name": "'+str(name)+'","tweet_text": "'+str(tweet)+'" } ,'
                print ('WTF = x = '+str(x))
                if (x==c-2):
                    fullTweet2='{"tweet_id": "'+str(tweet_id)+'","username": "'+str(username)+'","screen_name": "'+str(name)+'","tweet_text": "'+str(tweet)+'" } ]'
                saveTweet(fullTweet)
                saveTweet2(fullTweet2)
                tid=int(tweet_id)
                fullTweetCSV=str(tweet_id)+','+str(username)+','+str(name)+','+str(tweet)
                saveTweetCSV(fullTweetCSV)                
            except UnicodeEncodeError:
                print ('Tweet text not available - dodgy term in tweet broke the API')
                print ('---------------')
            x=x+1
    except KeyError:
        print ('twitter search terms broke the API')
        print ('---------------')
    
# ------------- end search twitter -------------------------

# ------------- get admin settings--------------------------
def loadAdmin (url):
    retrieveArray(adminURL)
    
    st=results[0] # get search term
    aa=st.split(',')
    global searchTerm
    searchTerm =aa[1]
    
    stype=results[1] # get search term
    bb=stype.split(',')
    global searchType
    searchType =bb[1]
    
    tNum=results[2] # get search term
    cc=tNum.split(',')
    global tweetNum
    tweetNum =cc[1]

    hPeriod=results[3] # get search term
    dd=hPeriod.split(',')
    global harvestPeriod
    harvestPeriod =dd[1]
    
    iText=results[4] # get search term
    ee=iText.split(',')
    global introText
    introText =ee[1]
    
    t2=results[5] # get search term
    ff=t2.split(',')
    global text2
    text2 =ff[1]
    print('-------- end of loadAdmin() ------------------')
    print('----------------------------------------------')
   
    
# ----------------------------------------------------------

# ------------- retrieve any google spreadsheet as data ----
def retrieveArray (url):
    Ws= requests.get(url)
    yy= Ws.text
    global results
    results = yy.splitlines()

    print ('stopwords ------------')
    print (results)
    print ('--------')

    print ('full list returned raw with line breaks --------')
    #print (yy)
    print ('results for '+url+' --------')
    # print (results)
    print ('--------')
    swCount=0
    for count in results:
        swCount+=1
    print ('count  for ' + url +'-----')
    print ('count = '+str(swCount))
    print (' end retrieveArray() ----------------------')
    # end retrieveArray
    
# ------------- end retrieve data ---------------------------
# ------------- end admin ad functions etc ------------------


# -----------------------------------------------------------
# ------------- the business starts here---------------------
# -----------------------------------------------------------

retrieveTweetIdJS()

loadAdmin (adminURL) #load admin settings from google sheet
retrieveArray(stopwordsURL) #load stopwords from stopwords google sheet

search_tweets(searchTerm,tweetNum) # execute the twitter API search using the admin settings loaded


def keeplooping():  # define the loop and what it executes (rate is set by loaded setting: 'harvestPeriod' 
   
    search_tweets(searchTerm,tweetNum)
    Timer(int(harvestPeriod), keeplooping).start()

keeplooping() # initiates the loop

# -----------------------------------------------------------
# ----------------- end busines -----------------------------


#search_tweets(searchTerm,searchType,tweetNum)
print ('-------99999999  end   9999-------')
print ('searchTerm = ')
print (searchTerm)
print ('searchType = ')
print (searchType)
print ('tweetNum')
print (tweetNum)
print ('harvestPeriod')
print (harvestPeriod)
print ('introText')
print (introText)
print ('text2')
print (text2)


print ('---- stopwords ------------')

