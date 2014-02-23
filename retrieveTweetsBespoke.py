import sqlite3 as lite # sqlite database
import sys
import requests
maxRet = 100 # limit returned
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

# -----------------------------------------------------------
def loadAdmin (url):
    retrieveArray(adminURL)
    
    st=results[0] # get search term
    aa=st.split(',')
    global searchTerm
    searchTerm =aa[1]

    x= searchTerm.find('#')
    y=searchTerm.find('@')
    global termTXT
    if x==0:
        term2 = searchTerm.split('#')[1] # strip off the hash
        termTXT= term2
    else:
        if y==0:
            print ('searching twitter API for username: @'+term)
            term3 = searchTerm.split('@')[1] # strip off the @
            termTXT= term3
        else:
            print ('searching for term: '+term) # or just search!
            termTXT= searchTerm
    
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
# -------------------   set up database    ------------------
def openDB (trm):
    dbName=str(trm)+'List.db'
    try:
        conb = lite.connect(dbName)
    except:
        print ('problem connecting in createDB() ')
    with conb: # has built in open and close db reources functionality apparently
        cur = conb.cursor()    
        cur.execute('SELECT count(*) FROM tweets')
        data2 = cur.fetchone()
        county=data2[0]
        print ('Start')
        print (str(county)+ ' records retrieved')
               

def last100 (trm): # get last row of database

    dbName=str(trm)+'List.db'
    try:
        conc = lite.connect(dbName)
    except:
        print ('problem connecting in createDB() ')
    with conc:
        cur = conc.cursor()
        cur.execute('SELECT count(*) FROM tweets')
        data2 = cur.fetchone()
        county=data2[0]
        print ('county =  '+str(county))
        subCounty = county
        cur.execute('SELECT * FROM tweets ORDER BY tid ASC LIMIT '+str(maxRet)) # return last (maxRet) records
        data3 = cur.fetchall()
        global x
        x=0
        while x<county:
            print (data3[x])
            print ('record '+str(x)+' of '+str(county))
            x=x+1
                                   
loadAdmin(adminURL)
last100(termTXT)
# --------------------  end db setup ------------------------
