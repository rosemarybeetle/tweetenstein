
function speakTest(speech)
{

console.log('test alert')
//var gurl= Trim('http://translate.google.com/translate_tts?ie=UTF-8&q='+speech);
console.log(speech);
//console.log(gurl);
document.getElementById('framer').src = 'http://translate.google.com/translate_tts?&tl=en-US&ie=UTF-8&q='+speech;
mouthoff(leng);
}
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
function swapMouth(le)

{
console.log ('le- '+le)
console.log ('mouthStop = '+mouthStop);
if (le > mouthStop)
{
console.log('if is working'); 
window.ran2= Math.floor((Math.random()*mouthNumber)+1);
console.log ('random number = '+ran2)
//console.log(leng);
imger = 'images/MOUTH-'+ran2+'.jpg';
window.mouthy.src=imger;
mouthStop+=1;
} else { 
console.log('if ELSE is working ');
mouthStop=0; // reset timer
clearInterval(gobo)
}
console.log('inside swapMouth');

}
function mouthoff(le)
{
window.mouthTimer=80;
window.gobo = setInterval(function(){swapMouth(le)},mouthTimer); //redraws a backgound to make the text visible
//swapMouth(le);
}
function harvestTweets ()
{
console.log('start harvestTweets');

$.getJSON( "tweetstore2.json", function(adata) {
console.log('l = '+adata.store.length);
l=adata.store.length; // set max 'l' based on length of imported array

$.each( adata.store, function(key,val) {
	//console.log('key= '+key,val.username,val.screen_name);
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
window.leng=1;
window.mouthStop=0; // counter needed by swapMouth
window.mouthNumber=8; // determines how many mouth images can be swapped
speakTest('hello there');
console.log ('Start setUp initialisation...');

window.l= 0;// used later to store array length
window.usernames = [];
window.screenames = [];
loadLastTweet ();

harvestTweets ();

// +++
console.log ("Hello, Tweetenstein.js...");
try {



myCanvas.width=W;
myCanvas.height = H;
myCanvas2.width=W;
myCanvas2.height = H;
var ctxt=document.getElementById("myCanvas");
window.txt=ctxt.getContext("2d");
window.fontDef="20px Arial";
txt.font=fontDef;
var ctxt2=document.getElementById("myCanvas2");
window.txt2=ctxt2.getContext("2d");
window.fontDef2="30px Arial";
txt2.font=fontDef2;

}
catch (e) { console.log("FAIL"+e)};
}
	);
	console.log('setUp complete!!!');
}
// -------------------------------end setup ---------------------

// speed of text draw
window.phi=100;
// speed of pulse
window.phi2=4000;
window.phi3=3500;
window.txty="Hello World...";
$( document ).ready(function() {
console.log ('document ready from intervals');
setInterval(function(){harvestTweets()}, phi2); // check for changes


});
window.onkeyup = keyup;
function keyup()
{
window.ran= Math.floor((Math.random()*l)+1);
console.log ('random number = '+ran)
console.log('inside keyup detection ');
window.g=screenames[ran];
window.leng=g.length;
speakTest(g);
 
}
$( document ).ready(function() {
setUp();
});
