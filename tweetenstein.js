/* --------------------------------------
-----------------------------------------
Andrew Lewis 2014
Canvas visualiser script to ingest tweet data and turn it into something else
v.1 31 Jan 2014 - test
github
*/

/* -------------
if (Modernizr.canvas) {
   console.log ("let's draw some shapes!")
} else {
   console.log("no native canvas support available :( ")
}
Optional test script to identify any elements (and handle them if necessary
------------------*/
function screenSize()
{
window.W=document.body.clientWidth;
window.H=document.body.clientHeight;
}
//-------------------------------Set Up------------------------
function yep() {
 console.log ('yep');
}
function loadLastTweet ()
{
$.getJSON( "lastTweet.json", function( data ) {
 console.log('start lastTweet');
  //console.log(data.lasttweetID);
  window.lasttweetID=data.lasttweetID;
  console.log(lasttweetID);
  console.log('Success from inside getJson call to lastTweet.json');
 });
}
function harvestTweets ()
{
console.log('start harvestTweets');
var twitems = [];
$.getJSON( "tweetstore2.json", function(adata) {
console.log('l = '+adata.store.length);
l=adata.store.length; // set max 'l' based on length of imported array
for ( var i = 0; i < l; i++ ) {
    $.each( adata.store, function(key,val) {
	
    console.log(key,val);
	
  });
  
  //console.log('twitems'+twitems);
	console.log('wtf')
    console.log(adata[i].username);
}

console.log('inside harvestTweets call to tweetstore.json');
 /*
 $.each( data, function() {
    console.log(data.username)
	//twitems.push( username, tweet_id );
  });
  console.log('twitems'+twitems);
  */
 });
 
}
function setUp() {
/* optional checking for html5 file apis, needed to read data
if (window.File && window.FileReader && window.FileList && window.Blob) {
  console.log("Yay - The File APIs are supported by your browser.")
} else {
  console.log('The File APIs are not fully supported by your browser.');
}*/
// +++
$( document ).ready(function() {
console.log ('Start setUp initialisation...');

loadLastTweet ();

harvestTweets ();

// +++
console.log ("Hello, Tweetenstein.js...");

screenSize();
myCanvas.width=W;
myCanvas.height = H;
var ctxt=document.getElementById("myCanvas");
window.txt=ctxt.getContext("2d");
window.fontDef="20px Arial";
txt.font=fontDef;
console.log('setUp complete!!!');
});
}
// -------------------------------end setup ---------------------


function plotLoop(txty){
screenSize();
window.xx=Math.random(1)*W-35;//initialise random x position variable;
window.yy=Math.random(1)*H;//initialise random y position variable;
txt.fillStyle="#86DDDE";
//txt.fillText(txty,xx,yy);
txt.fillText(lasttweetID,xx,yy);
}
function plotPulse() {
myCanvas.width=W;
myCanvas.height=H;
window.fontDef="20px Arial";
txt.font=fontDef;
}
// speed of text draw
window.phi=20;
// speed of pulse
window.phi2=4000;
window.txty="Hello World...";
$( document ).ready(function() {
console.log ('document ready from intervals');
setInterval(function(){plotPulse()},phi2); //redraws a backgound to make the text visible
setInterval(function(){plotLoop(txty)},phi); // fires out text at rate set by period: phi
});