import requests
import saveTweets
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
lastSavedTweetId=0

saveTweet=saveTweets.saveTweet
saveTweetCSV=saveTweetsCSV.saveTweet
saveTweetId=saveLastTweetId.saveTweetId


# -------------------   set up database    ------------------

def createDB ():
    con = lite.connect('tweetList.db')

    with con: # has built in open and close db reources functionality apparently
        cur = con.cursor()    
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        print ("SQLite version: %s"+ str(data)  )
        cur.execute("CREATE TABLE IF NOT EXISTS tweets(tid INT, UserName TEXT, ScreenName TEXT, Status TEXT)") # create A TABLE FOR THE FIRST TIME ONLY
        cur.execute('SELECT count(*) FROM tweets')
        data2 = cur.fetchone()
        print ('count  '+str(data2))

def createTermDB (term):
    dbName=str(term)+'List.db'
    con = lite.connect(dbName)

    with con: # has built in open and close db reources functionality apparently
        cur = con.cursor()    
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        print ("SQLite version: %s"+ str(data)  )
        cur.execute("CREATE TABLE IF NOT EXISTS tweets(tid INT, UserName TEXT, ScreenName TEXT, Status TEXT)") # create A TABLE FOR THE FIRST TIME ONLY
        cur.execute('SELECT count(*) FROM tweets')
        data2 = cur.fetchone()
        print ('count  '+str(data2))
        

def storeTweet (tid,un,nm,st) : #  this puts a record into the tweets database
    params=(tid,un,nm,st)
    conA = lite.connect('tweetList.db')
    with conA:
        cur = conA.cursor()
        cur.execute("INSERT INTO tweets VALUES(?,?,?,?)",params)
        

def lastTweet (): # get last row of database
    global lastSavedTweetId
    conA = lite.connect('tweetList.db')
    with conA:
        cur = conA.cursor()
        try:
            cur.execute('SELECT count(*) FROM tweets')
            data2 = cur.fetchone()
            county=data2[0]
            print ('count  '+str(county))
            cur.execute('SELECT max(tid) FROM tweets ') # shows highest value of a tweet_id in any record (i.e. the last one sent)
            data3 = cur.fetchone()
            lastSavedTweetId=data3[0]
            lastSavedTweetId=int(lastSavedTweetId)
            print('---------------')
            print ('ID of last tweet saved = '+str(lastSavedTweetId))
            print('---------------')
        except:
            print('tweetList database is empty')
            lastSavedTweet=0

def storeTermTweet (tid,un,nm,st) : #  this puts a record into the tweets database
    params=(tid,un,nm,st)
    dbName=str(termTXT)+'List.db'
    conA = lite.connect(dbName)
    with conA:
        cur = conA.cursor()
        cur.execute("INSERT INTO tweets VALUES(?,?,?,?)",params)
        

def lastTermTweet (): # get last row of database
    dbName=str(termTXT)+'List.db'
    conA = lite.connect(dbName)
    global lastSavedTweetId
    try:
        with conA:
            cur = conA.cursor()
            cur.execute('SELECT count(*) FROM tweets')
            data2 = cur.fetchone()
            county=data2[0]
            print ('count  '+str(county))
            cur.execute('SELECT max(tid) FROM tweets ') # shows highest value of a tweet_id in any record (i.e. the last one sent)
            data3 = cur.fetchone()
            lastSavedTweetId=data3[0]
            lastSavedTweetId=int(lastSavedTweetId)
            print('---------------')
            print ('ID of last tweet saved = '+str(lastSavedTweetId))
            print('---------------')
    except:
        print(termTXT+' database is empty')
        lastSavedTweet=0
        
        
# --------------------  end db setup ------------------------

#  --------------------------------------------------------------------------------------
#       ----------- end - above this line are set ups and imports etc ------------
#  --------------------------------------------------------------------------------------


# ------------- search twitter as a function ---------------
def search_tweets (term,t_type,count) : # params: term= 'what to search for' type = 'how to search' Count = 'number of tweets' (max 100)    search_url_root='https://api.twitter.com/1.1/search/tweets.json?q='
    # check what type the search term is
    
    search_url_root='https://api.twitter.com/1.1/search/tweets.json?q='
    x= term.find('#')
    y=term.find('@')
    global termTXT
    global rawTerm
    if x==0 : #  this is checking if the first character is a hashtag
        print ('searching twitter API for hashtag: '+term)
        term2 = term.split('#')[1] # strip off the hash
        termTXT= term2 # allows the search term to be passed as a parameter
        rawTerm=termTXT
        term='%23'+term2 # add unicode for # sign (%23) if a hashtag search term
        
    else:
        if y==0:
            print ('searching twitter API for username: @'+term)
            term3 = term.split('@')[1] # strip off the @
            termTXT= term3 # allows the search term to be passed as a parameter
            rawTerm=termTXT
            term='%40'+term3 # add unicode for @ sign (%40) if a username search
        else:
            print ('searching for term: '+term) # or just search!
            termTXT= term # allows the search term to be passed as a parameter
            rawTerm=termTXT
    
    
    search_url=str(search_url_root+term+'&count='+count)
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
        # lastTweetId=""
        lastTweet() 
        while (x<c):
            try:
                
                tweet_id = js['statuses'][x]['id']
                testID=int(tweet_id)
                print ('testID= '+str(testID))
                print ('lastSavedTweetId= '+str(lastSavedTweetId))
                print('-------')
                if testID>lastSavedTweetId and testID>0:
                    print('testID-lastSavedTweetId = '+str(testID-lastSavedTweetId))
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
                    print (tweet)
                    if (c-x>1):
                        fullTweet='{"tweet_id": "'+str(tweet_id)+'","username": "'+str(username)+'","screen_name": "'+str(name)+'","tweet_text": "'+str(tweet)+'" } '
                    else:
                        fullTweet='{"tweet_id": "'+str(tweet_id)+'","username": "'+str(username)+'","screen_name": "'+str(name)+'","tweet_text": "'+str(tweet)+'" } '
                
                    saveTweet(fullTweet)
                    tid=int(tweet_id)
                    storeTweet(tid,username,name,tweet)
                    #storeTermTweet(tid,username,name,tweet)
                    fullTweetCSV=str(tweet_id)+','+str(username)+','+str(name)+','+str(tweet)
                    saveTweetCSV(fullTweetCSV)
                else:
                    print('testID-lastSavedTweetId = '+str(testID-lastSavedTweetId))
            except UnicodeEncodeError:
                print ('Tweet text not available - dodgy term in tweet broke the API')
                print ('---------------')
            x=x+1
            #lastTweetId=str(tweet_id)
           
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
    print ('stopwords --------')
    # print (results)
    print ('--------')
    swCount=0
    for count in results:
        swCount+=1
    print ('count  -----')
    print ('count = '+str(swCount))
    # end retrieveArray
    
# ------------- end retrieve data ---------------------------

loadAdmin (adminURL) # go to Google drive and load admin setting (search terms etc)
retrieveArray(stopwordsURL) # go to Google drive and load stopword
search_tweets(searchTerm,searchType,tweetNum) #
createDB() 
createTermDB(termTXT) # Creates bespoke databases (depends on search term)
def keeplooping(): # defines loop
    #createTermDB(termTXT)
    search_tweets(searchTerm,searchType,tweetNum)
    Timer(30, keeplooping).start()

keeplooping() # initiates loop

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


