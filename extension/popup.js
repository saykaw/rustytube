document.addEventListener('DOMContentLoaded',function(){

    const btn = document.getElementById("summarise");

const inputfield= document.getElementById("query");
const verdict=document.getElementById("verdict");
const trans=document.getElementById("trans")
const keywrd=document.getElementById("keywords")
btn.addEventListener("click", function thisfunc() {
    btn.disabled = true;
    btn.innerHTML = "Summarising...";
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
        var url = tabs[0].url;
        var xhr = new XMLHttpRequest();
       xhr.open("GET", "http://127.0.0.1:5000/summary?url=" + url, true);
        xhr.onload = function myfunction() {
            var text = xhr.responseText;
            const p = document.getElementById("output");
            p.innerHTML = text;
            btn.disabled = false;
            btn.innerHTML = "Summarise";
        }
        xhr.send();
    });
}); 

const searchbtn=document.getElementById('Ask');
    searchbtn.addEventListener("click",function handlercode(e){

chrome.tabs.query({currentWindow:true,active:true},function(tabs){console.log('hlloo')
searchbtn.disabled=true;
searchbtn.innerHTML="hold on...";

var prompt=inputfield.value;
var xhr = new XMLHttpRequest();
var currentTabUrl = tabs[0].url;
var videourl = encodeURIComponent(currentTabUrl);
xhr.open("GET", "http://127.0.0.1:5000/response?query=" + encodeURIComponent(prompt) +
"&videourl=" + videourl, true);
xhr.onload = function myfunc1() {

    var text = xhr.responseText;
    const p = document.getElementById("answer");
    p.innerHTML = text;
    searchbtn.disabled = false;
    searchbtn.innerHTML="Ask!";
    }
xhr.send();})});


verdict.addEventListener("click",function(tabs){
    chrome.tabs.query({currentWindow:true,active:true},function(tabs){console.log('hlloo')

var xhr = new XMLHttpRequest();
var currentTabUrl = tabs[0].url;
var videourl = encodeURIComponent(currentTabUrl);
xhr.open("GET", "http://127.0.0.1:5000/verdict?videourl=" + videourl, true);
xhr.onload = function myfunc1() {

    var text = xhr.responseText;
    const p = document.getElementById("answer");
    p.innerHTML = text;
   verdict.disabled = false;

    }
xhr.send();})
})

trans.addEventListener("click",function(tabs){
    chrome.tabs.query({currentWindow:true,active:true},function(tabs){console.log('hlloo')

var xhr = new XMLHttpRequest();
var currentTabUrl = tabs[0].url;
var videourl = encodeURIComponent(currentTabUrl);
xhr.open("GET", "http://127.0.0.1:5000/transcription?videourl=" + videourl, true);
xhr.onload = function myfunc1() {

    var text = xhr.responseText;
    const p = document.getElementById("answer");
    p.innerHTML = text;
    trans.disabled = false;

    }
xhr.send();})
})



keywrd.addEventListener("click",function(tabs){
    chrome.tabs.query({currentWindow:true,active:true},function(tabs){console.log('hlloo')

var xhr = new XMLHttpRequest();
var currentTabUrl = tabs[0].url;
var videourl = encodeURIComponent(currentTabUrl);
xhr.open("GET", "http://127.0.0.1:5000/keywords?videourl=" + videourl, true);
xhr.onload = function myfunc1() {
    var text = xhr.responseText;
    const p = document.getElementById("answer");
    p.innerHTML = text;
    keywrd.disabled = false;


    }
xhr.send();})
})
    

})


    
    
    
    
    
    

