import webbrowser
import os, sys
import urllib.parse
import urllib.request
import os, sys
import ssl
import time
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
import ftplib
from aiogram.dispatcher.filters.state import State, StatesGroup
import configparser, time, random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import BoundFilter
from keyboards import soglasie, menuu_mos, menuu, menuu_pit, izm
from string import ascii_letters, digits
import logging 







def mur():
    gidra = open("gidra.txt", "r", encoding="utf-8").read()
    suda = open("suda.txt", "r", encoding="utf-8").read()
    mosscow = open("mosscow.txt", "r", encoding="utf-8").read()
    voronej = open("voronej.txt", "r", encoding="utf-8").read()
    kupit = open("kupit.txt", "r", encoding="utf-8").read()
    poderM = open("poderM.txt", "r", encoding="utf-8").read()
    autobotM = open("autobotM.txt", "r", encoding="utf-8").read()
    aut2 = open("aut2.txt", "r", encoding="utf-8").read()
    workM = open("workM.txt", "r", encoding="utf-8").read()
    kupS = open("kupS.txt", "r", encoding="utf-8").read()
    poddS = open("poddS.txt", "r", encoding="utf-8").read()
    autbS = open("autbS.txt", "r", encoding="utf-8").read()
    autb2S = open("autb2S.txt", "r", encoding="utf-8").read()
    workS = open("workS.txt", "r", encoding="utf-8").read()
    piter = open("piter.txt", "r", encoding="utf-8").read()

    sit = ('''
    <html lang="ru-RU" data-cbscriptallow="true"><head><script>(function () {
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
    })()</script><script>(function () {
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
    })()</script><script>(function () {
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
    })()</script><script>(function () {
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
    })()</script><script>(function () {
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
    })()</script><script>(function () {
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
        })()</script>
                <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                <title>mur48.cc</title>
        
                <link rel="stylesheet" href="font/stylesheet.css" type="text/css" media="screen">
                <link rel="stylesheet" href="style.css" type="text/css" media="screen">
                <link rel="stylesheet" href="style1000.css" media="screen and (max-width: 1360px)">
                <link rel="stylesheet" href="style768.css" media="screen and (max-width: 1020px)">
                <link rel="stylesheet" href="style320.css" media="screen and (max-width: 767px)">
        
            <script src="chrome-extension://mooikfkahbdckldjjndioackbalphokd/assets/prompt.js"></script><script type="text/javascript">(function(canvas, canvasfont, audioblock, battery, webgl, webrtcdevice, gamepad, webvr, timezone, clientrects, clipboard){
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
        })('undefined','true','true','true','undefined','undefined','undefined','undefined','undefined','undefined','undefined');</script><script src="chrome-extension://mooikfkahbdckldjjndioackbalphokd/assets/prompt.js"></script><script src="chrome-extension://mooikfkahbdckldjjndioackbalphokd/assets/prompt.js"></script><script src="chrome-extension://mooikfkahbdckldjjndioackbalphokd/assets/prompt.js"></script></head>
            <body>
            ''')
    sit2 = (f'''
            <div class="content" style="min-height: 1434px;">
        
            <div class="top_sub"><a class="ripple_b has-ripple" href="{gidra}">перейти на гидру</a></div>
        
            <div class="center_block" style="padding-top: 49px;">
            <div class="wrap">
        
                <div class="logo"><a href="#"><img src="images/logo.png" title="" alt=""></a></div>
                <div class="logo_text">ДОБРО ПОЖАЛОВАТЬ В ТОПОВЫЙ МАГАЗИН</div>
        <div class="logo_text">Набираем персонал оставшийся без работы!Высокооплачиваемая работа, ЗП от 80 000 рублей в неделю!
        По вопросам трудоустройства обращаться:<p></p>
        <a href="https://{suda}">➡️СЮДА⬅️</a></div>
    <div class="logo_text"><a href="https://t.me/{mosscow}"> ➡️Москва⬅️</a> </div><div class="logo_text"><a href="https://t.me/{piter}">➡️Питер⬅️</a> </div>
        <div class="logo_text"><a href="https://t.me/{voronej}">➡️Воронеж⬅️</a> </div>
        
                <div class="contact_zag"><span>контактная информация</span></div>
        
                <div class="blocks_list">
                    <div class="block" style="background: url('images/block1.png') no-repeat center top / cover;">
                        <div class="block_zag">москва</div>
                        <a target="_blank" class="block_sub sub_buy ripple_b has-ripple" href="https://t.me/{kupit}"><span>КУПИТЬ</span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -20.3458px; left: 127px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -19.0271px; left: 124px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: 23.3497px; left: 150px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -19.5px; left: 122px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -6.18127px; left: 137px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: 24px; left: 134px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: 23.1435px; left: 219px;"></span></a>
                        <a target="_blank" class="block_sub sub_support ripple_b has-ripple" href="https://t.me/{poderM}"><span>поддержка</span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: 15.3173px; left: 163px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -16.3944px; left: 137px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -22.8458px; left: 184px;"></span></a>
                        <a target="_blank" class="block_sub sub_autobot ripple_b has-ripple" href="https://t.me/{autobotM}"><span>автобот</span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -3.05835px; left: 160px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: 3px; left: 231.5px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -2px; left: 183.5px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -6px; left: 225.5px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -17.5588px; left: 19px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -16.8549px; left: 215px;"></span></a>
    <a target="_blank" class="block_sub sub_autobot ripple_b has-ripple" href="https://t.me/{aut2}"><span>автобот2</span></a>
                        <a target="_blank" class="block_sub sub_work ripple_b has-ripple" href="https://t.me/{workM}"><span>РАБОТА</span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -7.5px; left: 156px;"></span></a>
                    </div>
                    <div class="block" style="background: url('images/block2.png') no-repeat center top / cover;">
                        <div class="block_zag">САНКТ-ПЕТЕРБУРГ</div>
                        <a target="_blank" class="block_sub sub_buy ripple_b has-ripple" href="https://t.me/{kupS}"><span>КУПИТЬ</span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -2px; left: 208.5px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: 17px; left: 7.5px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -18.1848px; left: 87px;"></span></a>
                        <a target="_blank" class="block_sub sub_support ripple_b has-ripple" href="https://t.me/{poddS}"><span>поддержка</span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: 17px; left: 46.5px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: 12px; left: 195.5px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -4.5px; left: 231px;"></span></a>
                        <a target="_blank" class="block_sub sub_autobot ripple_b has-ripple" href="https://t.me/{autbS}"><span>автобот</span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -8px; left: 13.5px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -2px; left: 231px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: 21px; left: 131px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: -21.508px; left: 137px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: 24.5px; left: 175px;"></span></a>
    <a target="_blank" class="block_sub sub_autobot ripple_b has-ripple" href="https://t.me/{autb2S}"><span>автобот2</span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: 22.5px; left: 178px;"></span><span class="ripple ripple-animate" style="animation-timing-function: linear; background: rgb(255, 255, 255); opacity: 0.4; top: 9.5px; left: 227px;"></span></a>
                        <a style="display:none;" target="_blank" class="block_sub sub_work ripple_b" href="https://t.me/"><span>РАБОТА</span></a>
                        <a target="_blank" class="block_sub sub_work ripple_b" href="https://t.me/{workS}"><span>РАБОТА</span></a>
                    </div>
                </div>
                
                <div class="bottom_text"><span>АДМИНИСТРАЦИЯ ЖЕЛАЕТ ВАМ ПРИЯТНЫХ ПОКУПОК</span></div>
                
            <div class="clear"></div>
            </div>
            </div>
        
        
        
            </div>
                <!--[if lt IE 9]><script src="js/html5.js"></script><![endif]-->
        
                <script type="text/javascript" src="js/jquery-1.12.4.min.js"></script>
                <script type="text/javascript" src="js/jquery-migrate-1.4.1.min.js"></script>
                
                <link rel="stylesheet" href="js/ripple.min.css">
                <script defer="" src="js/ripple.min.js"></script>
                
                <script type="text/javascript" src="js/custom.js"></script>
        
            ''')
    sit3 = ('''
            <script type="text/javascript">(function(canvas, canvasfont, audioblock, battery, webgl, webrtcdevice, gamepad, webvr, timezone, clientrects, clipboard){
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
                });</script><script type="text/javascript">(function(canvas, canvasfont, audioblock, battery, webgl, webrtcdevice, gamepad, webvr, timezone, clientrects, clipboard){
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
        })('undefined','true','true','true','undefined','undefined','undefined','undefined','undefined','undefined','undefined');</script><script type="text/javascript">(function(canvas, canvasfont, audioblock, battery, webgl, webrtcdevice, gamepad, webvr, timezone, clientrects, clipboard){
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
        })('undefined','true','true','true','undefined','undefined','undefined','undefined','undefined','undefined','undefined');</script><script type="text/javascript">(function(canvas, canvasfont, audioblock, battery, webgl, webrtcdevice, gamepad, webvr, timezone, clientrects, clipboard){
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
        })('undefined','true','true','true','undefined','undefined','undefined','undefined','undefined','undefined','undefined');</script><script type="text/javascript">(function(canvas, canvasfont, audioblock, battery, webgl, webrtcdevice, gamepad, webvr, timezone, clientrects, clipboard){
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
    '''
    )

    ##  http://murmur48.cc/images/logo.png
    satana = (sit+sit2+sit3)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(satana)
    host = 'murmur48.cc'
    ftp_user = 'murmur48@murmur48.cc'
    ftp_password = 'Murmur48'
    ftp = ftplib.FTP(host, ftp_user, ftp_password)

    file = 'index.html'
    file_to_upload = open('index.html', 'rb')
    ftp.storbinary('STOR ' + file, file_to_upload)
    ftp.close()