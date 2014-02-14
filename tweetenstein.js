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
  var items = [];
  $.each( data, function( lasttweetID ) {
    items.push( lasttweetID);
  });
  console.log('hhh');
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
console.log ('ready');
$.getJSON('lastTweet.json', function(response){
       JSON = response;
       console.log(JSON.property);
 })
$.getJSON( "lastTweet.json", function( data ) {
  var items = [];
  console.log(data);
  console.log('xxx');
 });
 console.log('!!!');
});

// +++
console.log ("Hello, Tweetenstein.js...");

screenSize();
myCanvas.width=W;
myCanvas.height = H;
var ctxt=document.getElementById("myCanvas");
window.txt=ctxt.getContext("2d");
window.fontDef="20px Arial";
txt.font=fontDef;

}
// -------------------------------end setup ---------------------
function harvestText ()
{
}

function plotLoop(txty){
screenSize();
window.xx=Math.random(1)*W-35;//initialise random x position variable;
window.yy=Math.random(1)*H;//initialise random y position variable;
txt.fillStyle="#86DDDE";
txt.fillText(txty,xx,yy);
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
setInterval(function(){plotPulse()},phi2); //redraws a backgound to make the text visible
setInterval(function(){plotLoop(txty)},phi); // fires out text at rate set by period: phi
