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

$.getJSON( "tweetstore2.json", function(adata) {
console.log('l = '+adata.store.length);
l=adata.store.length; // set max 'l' based on length of imported array

$.each( adata.store, function(key,val) {
	console.log('key= '+key,val.username,val.screen_name);
	usernames.push (val.username);
	screenames.push (val.screen_name)

	
	
	
  }  );
  
  console.log(usernames);
  console.log(screenames);
	console.log('wtf')
    //console.log(adata[i].username);
//for ( var i = 0; i < l; i++ ) {
//}

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

window.l= 0;// used later to stotre array length
window.usernames = [];
window.screenames = [];
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
var ctxt=document.getElementById("myCanvas2");
window.txt2=ctxt.getContext("2d");
window.fontDef2="30px Arial";
txt2.font=fontDef2;
console.log('setUp complete!!!');
});
}
// -------------------------------end setup ---------------------


function plotLoop(txty){
screenSize();
window.xx=Math.random(1)*W-35;//initialise random x position variable;
window.yy=Math.random(1)*H;//initialise random y position variable;
window.xx2=Math.random(1)*W-35;//initialise random x position variable;
window.yy2=Math.random(1)*H;//initialise random y position variable;
txt.fillStyle="yellow";
txt2.fillStyle="purple";
//txt.fillText(txty,xx,yy);
ran= Math.floor((Math.random()*l)+1);
console.log ('random number = '+ran)
//txt.fillText(lasttweetID,xx,yy);
txt.fillText(screenames[ran],xx,yy);
txt2.fillText(usernames[ran],xx2,yy2);
}
function plotPulse() {
myCanvas.width=W;
myCanvas.height=H;
window.fontDef="20px Arial";
txt.font=fontDef;
txt2.font=fontDef2;
}
// speed of text draw
window.phi=70;
// speed of pulse
window.phi2=4000;
window.txty="Hello World...";
$( document ).ready(function() {
console.log ('document ready from intervals');
setInterval(function(){plotPulse()},phi2); //redraws a backgound to make the text visible
setInterval(function(){harvestTweets()}, phi2); // check for changes
setInterval(function(){plotLoop(txty)},phi); // fires out text at rate set by period: phi
});