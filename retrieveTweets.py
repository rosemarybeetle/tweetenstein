import sqlite3 as lite # sqlite database
import sys
maxRet = 100 # limit returned

# -------------------   set up database    ------------------
conb = lite.connect('tweetList.db')

with conb: # has built in open and close db reources functionality apparently
    cur = conb.cursor()    
    cur.execute('SELECT count(*) FROM tweets')
    data2 = cur.fetchone()
    county=data2[0]
    print ('Start')
    print (str(county)+ ' records retrieved')
               

def last100 (): # get last row of database
    conc = lite.connect('tweetList.db')
    with conc:
        cur = conc.cursor()
        cur.execute('SELECT count(*) FROM tweets')
        data2 = cur.fetchone()
        county=data2[0]
        print ('count  '+str(county))
        subCounty = county
        cur.execute('SELECT * FROM tweets ORDER BY tid DESC LIMIT '+str(maxRet)) # return last (maxRet) records
        data3 = cur.fetchall()
        global x
        x=0
        while x<county:
            print (data3[x])
            print ('record '+str(x)+' of '+str(county))
            x=x+1
                                   

last100()
# --------------------  end db setup ------------------------
