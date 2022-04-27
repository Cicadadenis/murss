import os
import urllib.parse
import urllib.request
import os, sys
import ssl
import ftplib



def ttt():
        
    rabota = open("3/rb.txt", "r", encoding="utf-8").read()
    suda = open("3/suda.txt", "r", encoding="utf-8").read()
    fon = open("3/fon.txt", "r", encoding="utf-8").read()
    biz = open("3/biz.txt", "r", encoding="utf-8").read()
    sha = open("3/sha.txt", "r", encoding="utf-8").read()
    ser = open("3/ser.txt", "r", encoding="utf-8").read()



    sit = ('''

    <html data-cbscriptallow="true"><script async="" src="https://www.google-analytics.com/analytics.js"></script><script>(function () {
    const toBlob = HTMLCanvasElement.prototype.toBlob;
    const toDataURL = HTMLCanvasElement.prototype.toDataURL;
    const getImageData = CanvasRenderingContext2D.prototype.getImageData;
    //
    var noisify = function (canvas, context) {
        const shift = {
        'r': Math.floor(Math.random() * 10) - 5,
        'g': Math.floor(Math.random() * 10) - 5,
        'b': Math.floor(Math.random() * 10) - 5,
        'a': Math.floor(Math.random() * 10) - 5
        };
        //
        const width = canvas.width, height = canvas.height;
        const imageData = getImageData.apply(context, [0, 0, width, height]);
        for (let i = 0; i < height; i++) {
        for (let j = 0; j < width; j++) {
            const n = ((i * (width * 4)) + (j * 4));
            imageData.data[n + 0] = imageData.data[n + 0] + shift.r;
            imageData.data[n + 1] = imageData.data[n + 1] + shift.g;
            imageData.data[n + 2] = imageData.data[n + 2] + shift.b;
            imageData.data[n + 3] = imageData.data[n + 3] + shift.a;
        }
        }
        //
        window.top.postMessage("canvas-fingerprint-defender-alert", '*');
        context.putImageData(imageData, 0, 0);
    };
    //
    Object.defineProperty(HTMLCanvasElement.prototype, "toBlob", {
        "value": function () {
        noisify(this, this.getContext("2d"));
        return toBlob.apply(this, arguments);
        }
    });
    //
    Object.defineProperty(HTMLCanvasElement.prototype, "toDataURL", {
        "value": function () {
        noisify(this, this.getContext("2d"));
        return toDataURL.apply(this, arguments);
        }
    });
    //
    Object.defineProperty(CanvasRenderingContext2D.prototype, "getImageData", {
        "value": function () {
        noisify(this.canvas, this);
        return getImageData.apply(this, arguments);
        }
    });
    //
    document.documentElement.dataset.cbscriptallow = true;
    })()</script><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>
    * { box-sizing: border-box; margin: 0; padding: 0 }
    #__next {
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    #crisp-chatbox > div[class^="crisp-"] > a[class^="crisp-"] {
        bottom: 54px !important;
    }
    </style><meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1"><meta charset="utf-8"><title>ABAWORK</title><meta name="og:title" content="ABAWORK"><meta name="twitter:title" content="ABAWORK"><meta name="og:site_name" content="ABAWORK"><meta name="og:image" content="https://airsite.nyc3.cdn.digitaloceanspaces.com/brand/icon-256.png"><meta name="twitter:image" content="https://airsite.nyc3.cdn.digitaloceanspaces.com/brand/icon-256.png"><meta name="og:type" content="website"><meta name="twitter:card" content="summary"><link rel="canonical" href="/"><link rel="shortcut icon" href="null"><meta name="next-head-count" content="12"><link rel="preload" href="/_next/static/tNYwbe886hnDv9uF7cXjt/pages/index.js" as="script"><link rel="preload" href="/_next/static/tNYwbe886hnDv9uF7cXjt/pages/_app.js" as="script"><link rel="preload" href="/_next/static/runtime/webpack-5247482ebcd811c9f929.js" as="script"><link rel="preload" href="/_next/static/chunks/framework.1da4ef788d111291b4b6.js" as="script"><link rel="preload" href="/_next/static/chunks/commons.4cf1157854d94d82078f.js" as="script"><link rel="preload" href="/_next/static/chunks/d22e4f5c724d666750fe44516895f703072ed09f.7b1b72c2c4e99b5a67d6.js" as="script"><link rel="preload" href="/_next/static/runtime/main-cb29ba5623faf6e6dfd1.js" as="script"><link rel="preload" href="/_next/static/chunks/151566a4651e83b50223f84eab66dbab6954d29f.7d68887e701c477e5f78.js" as="script"><link rel="preload" href="/_next/static/chunks/be4ce260d173322dd4ddf7dc70532fb96bd360d4.0efdea021efae6576dac.js" as="script"><style>

    html, body, #__next {
    width: 100%;
    /* To smooth any scrolling behavior */
    -webkit-overflow-scrolling: touch;
    margin: 0px;
    padding: 0px;
    /* Allows content to fill the viewport and go beyond the bottom */
    min-height: 100%;
    }
    #__next {
    flex-shrink: 0;
    flex-basis: auto;
    flex-direction: column;
    flex-grow: 1;
    display: flex;
    flex: 1;
    }
    html {
    scroll-behavior: smooth;
    /* Prevent text size change on orientation change https://gist.github.com/tfausak/2222823#file-ios-8-web-app-html-L138 */
    -webkit-text-size-adjust: 100%;
    height: 100%;
    }
    body {
    display: flex;
    /* Allows you to scroll below the viewport; default value is visible */
    overflow-y: auto;
    overscroll-behavior-y: none;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    -ms-overflow-style: scrollbar;
    }
    </style><style id="react-native-stylesheet">[stylesheet-group="0"]{}
    html{-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;-webkit-tap-highlight-color:rgba(0,0,0,0);}
    body{margin:0;}
    button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0;}
    input::-webkit-inner-spin-button,input::-webkit-outer-spin-button,input::-webkit-search-cancel-button,input::-webkit-search-decoration,input::-webkit-search-results-button,input::-webkit-search-results-decoration{display:none;}
    [stylesheet-group="0.1"]{}
    :focus:not([data-focusvisible-polyfill]){outline: none;}
    [stylesheet-group="0.5"]{}
    .css-4rbku5{background-color:rgba(0,0,0,0.00);color:inherit;font:inherit;list-style:none;margin-bottom:0px;margin-left:0px;margin-right:0px;margin-top:0px;text-align:inherit;text-decoration:none;}
    .css-18t94o4{cursor:pointer;}
    [stylesheet-group="1"]{}
    .css-1dbjc4n{-ms-flex-align:stretch;-ms-flex-direction:column;-ms-flex-negative:0;-ms-flex-preferred-size:auto;-webkit-align-items:stretch;-webkit-box-align:stretch;-webkit-box-direction:normal;-webkit-box-orient:vertical;-webkit-flex-basis:auto;-webkit-flex-direction:column;-webkit-flex-shrink:0;align-items:stretch;border:0 solid black;box-sizing:border-box;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-webkit-flex;display:flex;flex-basis:auto;flex-direction:column;flex-shrink:0;margin-bottom:0px;margin-left:0px;margin-right:0px;margin-top:0px;min-height:0px;min-width:0px;padding-bottom:0px;padding-left:0px;padding-right:0px;padding-top:0px;position:relative;z-index:0;}
    .css-901oao{border:0 solid black;box-sizing:border-box;color:rgba(0,0,0,1.00);display:inline;font:14px system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Ubuntu,"Helvetica Neue",sans-serif;margin-bottom:0px;margin-left:0px;margin-right:0px;margin-top:0px;padding-bottom:0px;padding-left:0px;padding-right:0px;padding-top:0px;white-space:pre-wrap;word-wrap:break-word;}
    .css-9pa8cd{bottom:0px;height:100%;left:0px;opacity:0;position:absolute;right:0px;top:0px;width:100%;z-index:-1;}
    [stylesheet-group="2"]{}
    .r-1udh08x{overflow-x:hidden;overflow-y:hidden;}
    .r-10vs3n6{border-bottom-color:rgba(199,206,211,1.00);border-left-color:rgba(199,206,211,1.00);border-right-color:rgba(199,206,211,1.00);border-top-color:rgba(199,206,211,1.00);}
    .r-z2wwpe{border-bottom-left-radius:4px;border-bottom-right-radius:4px;border-top-left-radius:4px;border-top-right-radius:4px;}
    .r-1phboty{border-bottom-style:solid;border-left-style:solid;border-right-style:solid;border-top-style:solid;}
    .r-rs99b7{border-bottom-width:1px;border-left-width:1px;border-right-width:1px;border-top-width:1px;}
    [stylesheet-group="2.1"]{}
    .r-1pn2ns4{padding-left:8px;padding-right:8px;}
    .r-oyd9sg{padding-bottom:4px;padding-top:4px;}
    [stylesheet-group="2.2"]{}
    .r-1awozwy{-ms-flex-align:center;-webkit-align-items:center;-webkit-box-align:center;align-items:center;}
    .r-1777fci{-ms-flex-pack:center;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;}
    .r-z80fyv{height:20px;}
    .r-19wmn03{width:20px;}
    .r-17bb2tj{-webkit-animation-duration:0.75s;animation-duration:0.75s;}
    .r-1muvv40{-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite;}
    .r-127358a{-webkit-animation-name:r-9p3sdl;animation-name:r-9p3sdl;}
    @-webkit-keyframes r-9p3sdl{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg);}100%{-webkit-transform:rotate(360deg);transform:rotate(360deg);}}
    @keyframes r-9p3sdl{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg);}100%{-webkit-transform:rotate(360deg);transform:rotate(360deg);}}
    .r-1ldzwu0{-webkit-animation-timing-function:linear;animation-timing-function:linear;}
    .r-1pi2tsx{height:100%;}
    .r-13qz1uu{width:100%;}
    .r-2llsf{min-height:100%;}
    .r-g6jmlv{width:100vw;}
    .r-1mlwlqe{-ms-flex-preferred-size:auto;-webkit-flex-basis:auto;flex-basis:auto;}
    .r-417010{z-index:0;}
    .r-1niwhzg{background-color:rgba(0,0,0,0.00);}
    .r-vvn4in{background-position:center;}
    .r-u6sd8q{background-repeat:no-repeat;}
    .r-4gszlv{background-size:cover;}
    .r-1p0dtai{bottom:0px;}
    .r-1d2f490{left:0px;}
    .r-u8s1d{position:absolute;}
    .r-zchlnj{right:0px;}
    .r-ipm5af{top:0px;}
    .r-1wyyakw{z-index:-1;}
    .r-14lw9ot{background-color:rgba(255,255,255,1.00);}
    .r-1ebgqk7{bottom:10px;}
    .r-14vhaug{box-shadow:1px 1px 4px rgba(68,78,87,0.30);}
    .r-18u37iz{-ms-flex-direction:row;-webkit-box-direction:normal;-webkit-box-orient:horizontal;-webkit-flex-direction:row;flex-direction:row;}
    .r-1xcajam{position:fixed;}</style></head>''')
    sit2 = (f'''
    <body style="height:100%;overflow:scroll"><div id="__next"><div class="css-1dbjc4n r-1pi2tsx r-13qz1uu"><div class="css-1dbjc4n r-1777fci r-2llsf r-g6jmlv"><div class="css-1dbjc4n r-1p0dtai r-1d2f490 r-1xcajam r-zchlnj r-ipm5af" style="background-color:rgba(0,0,0,0.60)"><div class="css-1dbjc4n r-1p0dtai r-1mlwlqe r-1d2f490 r-1udh08x r-u8s1d r-zchlnj r-ipm5af r-1wyyakw"><div class="css-1dbjc4n r-1niwhzg r-vvn4in r-u6sd8q r-4gszlv r-1p0dtai r-1pi2tsx r-1d2f490 r-u8s1d r-zchlnj r-ipm5af r-13qz1uu r-1wyyakw" style="background-image: url({fon});"></div><img alt="" draggable="false" src="{fon}" class="css-9pa8cd"></div><div class="css-1dbjc4n r-1p0dtai r-1d2f490 r-1xcajam r-zchlnj r-ipm5af" style="background-color:rgba(0,0,0,0.60)"></div></div><div class="css-1dbjc4n r-1777fci" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch" data-testid="blockContainer-undefined"><div class="css-1dbjc4n r-1777fci r-2llsf r-13qz1uu"><div class="css-1dbjc4n r-1777fci r-13qz1uu" style="-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;padding-right:13.333333333333334px;padding-left:13.333333333333334px;padding-bottom:40px;-webkit-box-orient:vertical;-webkit-box-direction:normal" data-testid="viewBlock-undefined"><div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 65px;"><div class="css-1dbjc4n r-1777fci" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch" data-testid="blockContainer-undefined"><div class="css-1dbjc4n r-1777fci r-2llsf r-13qz1uu"><div class="css-1dbjc4n r-1777fci r-13qz1uu" style="-webkit-align-self:center;align-self:center;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;padding-right:13.333333333333334px;padding-left:13.333333333333334px;padding-top:40px;padding-bottom:40px;-ms-flex-item-align:center;-webkit-box-orient:vertical;-webkit-box-direction:normal" data-testid="viewBlock-undefined"><div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 65px;"><div class="css-1dbjc4n r-1777fci" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch" data-testid="blockContainer-undefined"><div class="css-1dbjc4n r-1777fci r-13qz1uu" style="background-image: linear-gradient(0deg, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0));"><div class="css-1dbjc4n r-1awozwy r-1777fci r-13qz1uu" style="align-self: center; flex-direction: column; padding: 0px; -webkit-box-orient: vertical; -webkit-box-direction: normal; max-width: 420px;" data-testid="viewBlock-undefined"><div class="css-1dbjc4n r-1777fci r-417010" style="-webkit-flex-shrink:1;flex-shrink:1;max-width:100%;-ms-flex-negative:1"><div class="css-1dbjc4n r-1777fci" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch" data-testid="blockContainer-undefined"><div class="css-1dbjc4n r-1777fci r-13qz1uu"><div class="css-1dbjc4n r-18u37iz r-1777fci r-13qz1uu" style="padding: 16px 0px; max-width: 420px;" data-testid="viewBlock-undefined"><div class="css-1dbjc4n r-1777fci r-417010" style="-webkit-flex-shrink:1;flex-shrink:1;max-width:100%;-ms-flex-negative:1"><div class="css-1dbjc4n r-1awozwy r-1777fci" style="max-width:100%" data-testid="blockContainer-undefined"><div dir="auto" class="css-901oao" style="align-self: center; color: rgb(255, 255, 255); font-size: 30px; font-weight: 400;  text-align: center; max-width: 420px;" data-testid="textBlock-undefined">
    {sha}
    <a href="https://t.me/{suda}">➡️СЮДА⬅️</a>

    ИЛИ НА    
    
    <a href="{biz}">➡️САЙТЕ⬅️</a>

    {ser}''')

    sit3 = ('''


    <script async="" data-next-page="/_app" src="/_next/static/tNYwbe886hnDv9uF7cXjt/pages/_app.js"></script><script src="/_next/static/runtime/webpack-5247482ebcd811c9f929.js" async=""></script><script src="/_next/static/chunks/framework.1da4ef788d111291b4b6.js" async=""></script><script src="/_next/static/chunks/commons.4cf1157854d94d82078f.js" async=""></script><script src="/_next/static/chunks/d22e4f5c724d666750fe44516895f703072ed09f.7b1b72c2c4e99b5a67d6.js" async=""></script><script src="/_next/static/runtime/main-cb29ba5623faf6e6dfd1.js" async=""></script><script src="/_next/static/chunks/151566a4651e83b50223f84eab66dbab6954d29f.7d68887e701c477e5f78.js" async=""></script><script src="/_next/static/chunks/be4ce260d173322dd4ddf7dc70532fb96bd360d4.0efdea021efae6576dac.js" async=""></script><script src="/_next/static/tNYwbe886hnDv9uF7cXjt/_buildManifest.js" async=""></script></body><script type="text/javascript">(function(canvas, canvasfont, audioblock, battery, webgl, webrtcdevice, gamepad, webvr, timezone, clientrects, clipboard){
            function processFunctions(scope) {

                console.log("audioblock"+audioblock);
                if (audioblock == 'true') {
                    var audioblock_triggerblock = scope.document.createElement('div');
                    audioblock_triggerblock.className = 'browsesafe_heedlljjfegnjeijpnkbhpofeejflkea_audio';
                    var audioblock_a = scope.AudioBuffer;
                    audioblock_a.prototype.copyFromChannel = function() {
                        audioblock_triggerblock.title = 'copyFromChannel';
                        document.documentElement.appendChild(audioblock_triggerblock);
                        return false;
                    }
                    audioblock_a.prototype.getChannelData = function() {
                        audioblock_triggerblock.title = 'getChannelData';
                        document.documentElement.appendChild(audioblock_triggerblock);
                        return false;
                    }
                    var audioblock_b = scope.AnalyserNode;
                    audioblock_b.prototype.getFloatFrequencyData = function() {
                        audioblock_triggerblock.title = 'getFloatFrequencyData';
                        document.documentElement.appendChild(audioblock_triggerblock);
                        return false;
                    }
                    audioblock_b.prototype.getByteFrequencyData = function() {
                        audioblock_triggerblock.title = 'getByteFrequencyData';
                        document.documentElement.appendChild(audioblock_triggerblock);
                        return false;
                    }
                    audioblock_b.prototype.getFloatTimeDomainData = function() {
                        audioblock_triggerblock.title = 'getFloatTimeDomainData';
                        document.documentElement.appendChild(audioblock_triggerblock);
                        return false;
                    }
                    audioblock_b.prototype.getByteTimeDomainData = function() {
                        audioblock_triggerblock.title = 'getByteTimeDomainData';
                        document.documentElement.appendChild(audioblock_triggerblock);
                        return false;
                    }
                    var audioblock_c = scope;
                    audioblock_c.AudioContext = function() {
                        audioblock_triggerblock.title = 'AudioContext';
                        document.documentElement.appendChild(audioblock_triggerblock);
                        return false;
                    }
                    audioblock_c.webkitAudioContext = function() {
                        audioblock_triggerblock.title = 'webkitAudioContext';
                        document.documentElement.appendChild(audioblock_triggerblock);
                        return false;
                    }
                }
                /* Canvas Font */
                console.log("canvasfont = "+canvasfont);
                if (canvasfont == 'true') {
                    var canvasfont_triggerblock = scope.document.createElement('div');
                    canvasfont_triggerblock.className = 'browsesafe_heedlljjfegnjeijpnkbhpofeejflkea_canvasfont';
                    var canvasfont_a = scope.CanvasRenderingContext2D;
                    canvasfont_a.prototype.measureText = function() {
                        canvasfont_triggerblock.title = 'measureText';
                        document.documentElement.appendChild(canvasfont_triggerblock);
                        return false;
                    }
                }
                /* Battery */
                if (battery == 'true') {
                    var battery_triggerblock = scope.document.createElement('div');
                    battery_triggerblock.className = 'browsesafe_heedlljjfegnjeijpnkbhpofeejflkea_battery';
                    var battery_a = scope.navigator;
                    battery_a.getBattery = function() {
                        battery_triggerblock.title = 'getBattery';
                        document.documentElement.appendChild(battery_triggerblock);
                        return void(0);
                    }
                }
            
            }
            processFunctions(window);
            var iwin = HTMLIFrameElement.prototype.__lookupGetter__('contentWindow'), idoc = HTMLIFrameElement.prototype.__lookupGetter__('contentDocument');
            Object.defineProperties(HTMLIFrameElement.prototype, {
                contentWindow: {
                    get: function() {
                        var frame = iwin.apply(this);
                        if (this.src && this.src.indexOf('//') != -1 && location.host != this.src.split('/')[2]) return frame;
                        try { frame.HTMLCanvasElement } catch (err) { /* do nothing*/ }
                        processFunctions(frame);
                        return frame;
                    }
                },
                contentDocument: {
                    get: function() {
                        if (this.src && this.src.indexOf('//') != -1 && location.host != this.src.split('/')[2]) return idoc.apply(this);
                        var frame = iwin.apply(this);
                        try { frame.HTMLCanvasElement } catch (err) { /* do nothing*/ }
                        processFunctions(frame);
                        return idoc.apply(this);
                    }
                }
            });
        })('undefined','true','true','true','undefined','undefined','undefined','undefined','undefined','undefined','undefined');</script></html>
        ''')
    sit4 = f'<div class="css-1dbjc4n r-1awozwy r-1777fci" style="max-width:100%" data-testid="blockContainer-undefined"><a href="https://t.me/{rabota}" target="_blank" role="link" data-focusable="true" class="css-4rbku5 css-18t94o4 css-1dbjc4n" style="max-width:100%" rel=" noopener noreferrer"><div class="css-1dbjc4n r-rs99b7 r-1777fci" style="-webkit-align-self:center;align-self:center;border-top-color:rgba(241,196,15,1.00);border-right-color:rgba(241,196,15,1.00);border-bottom-color:rgba(241,196,15,1.00);border-left-color:rgba(241,196,15,1.00);border-top-left-radius:26.666666666666668px;border-top-right-radius:26.666666666666668px;border-bottom-right-radius:26.666666666666668px;border-bottom-left-radius:26.666666666666668px;height:64px;margin-right:16px;margin-left:16px;margin-top:13.333333333333334px;margin-bottom:13.333333333333334px;max-width:288px;width:256px;-ms-flex-item-align:center" data-testid="buttonBlock-undefined"><div dir="auto" class="css-901oao" style="color:rgba(241,196,15,1.00);font-size:16px;font-weight:600;text-align:center">РАБОТА</div></div></a></div>'
    sait = sit+sit2+sit3+sit4

    with open("3/index.html", "w", encoding="utf-8") as f:
        f.write(sait)

#       aba@abawork.cc

    #host = 'murmur48.cc'
    #ftp_user = 'aba@abawork.cc'
    #ftp_password = 'Tramadol1989'
    #ftp = ftplib.FTP(host, ftp_user, ftp_password)
#
    #file = 'index.html'
    #file_to_upload = open('3/index.html', 'rb')
    #ftp.storbinary('STOR ' + file, file_to_upload)
    #ftp.close()
#