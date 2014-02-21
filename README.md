tweetenstein
============

tweet-based physical interactive thing
A.Lewis. Started January 2014

The eventual out come of this will be to provide the brains for a physical interactive.
The intention is to create a self-contained unit using a Raspberry Pi running Python to access web data from Google, Twitter as required and manipulate and store it.

A python web server will run on the Pi (simpleserver.py) (this is needed to load local files stored in same directory as localhost/
Additionally a harvesting python script (getTweets.py) loads admin settings from Google Drive (publishing to the web as .txt)
getTweets makes a call to the twitter API using OAUTH (using twitter app keys etc)
It saves an initial dump of n tweets (m-max = 100) as a text file 
It saves a JSON file with the last retrieved tweet in it

A html5 page creates the visual display using <canvas> (visualisor.html)
Visualisor has a linked javascript file (tweetenstein.js)
And a CSS style sheet (styler.css) 


more to follow...

Actual final concept and shape of the interactive tbc. 
