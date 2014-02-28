# retrieveTweetsStoreContents
import json
def retrieveTweetStore ():
    savedTweets = open('tweetstore2.json', 'r')
    cons = savedTweets.read()
    tweets = json.loads(cons)
    # astSavedTweetIdJS
    # lastSavedTweetIdJS=ltids['lasttweetID']
    
    print ('-------------')
    print ('-------------')
   
    print('cons = '+cons)
   
    print ('-------------')
    print ('-------------')
    savedTweets.close()
retrieveTweetStore()

