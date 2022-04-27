import requests
from murmur import mur
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
from pathlib import Path
from os.path import exists
from datetime import datetime
import requests, os
from io import BytesIO
import aiohttp
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import BoundFilter
from klava import soglasie, menuu, izm, menuu_mos, menuu_pit, otm
from string import ascii_letters, digits
import logging 
token = "5246005528:AAHLdEQzSBJ33RozYVoK2LqoQqUNR-9SuP0"
bot = Bot(token=token,parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

class PhotoStorage:
    def __init__(self, path: str):
        self.path = path
        self.data = self.load()
    
    def load(self):
        if exists(self.path):
            with open(self.path) as file:
                return file.readlines()


async def upload_document(
    bot, doc: types.photo_size.PhotoSize or types.Document
) -> str:
    with await doc.download(BytesIO()) as file:

        form = aiohttp.FormData()
        form.add_field(
            name="file",
            value=file,
        )

        async with bot.session.post("https://telegra.ph/upload", data=form) as response:
            img_src = await response.json()

    return "http://telegra.ph/" + img_src[0]["src"]
baza = []
class akasil(StatesGroup):
    bot2 = State()
    otziv = State()
    biz = State()
    mzmz = State()
    ffff = State()
    wiwi = State()
    name = State()
    forum = State()
    bott = State()
    tex = State()
    zzz = State()
    oper = State()
    bzbz = State()
    img1 = State()
    img2 = State()
    ss = State()
    izob3 = State()
    parol = State()
    bot22 = State()
    otziv2 = State()
    biz2 = State()
    forum2 = State()
    bott2 = State()
    tex2 = State()
    oper2 = State()
    img12 = State()
    img22 = State()
    parol2 = State()

#
#@dp.message_handler(content_types=types.ContentTypes.ANY)
#async def start_command(message: types.Message):
#    await message.answer(message)
den = "CAACAgQAAxkBAAIJ8GJb97iGZboPRLkU1bW3_qc526zOAAL7DgAC0bqZUB-bxAQhETNaJAQ"
st = "CAACAgQAAxkBAAIJ8GJb97iGZboPRLkU1bW3_qc526zOAAL7DgAC0bqZUB-bxAQhETNaJAQ"
@dp.message_handler(commands=['start'], state='*')
async def start_command(message: types.Message, state: FSMContext):
    await state.finish()
    imya = message.chat.first_name
    chat_id = message.chat.id
    if chat_id not in baza:
        await message.answer(
            f"<b>Привет  {imya} </b>\n\n"
            f"<b>Тебя Нет В Базе \nАвторизуйся Для Пользованиям Этим Ботом</b>\n\n")
        time.sleep(3)
        await message.answer("<b>Введи Пароль:  </b>")
        await akasil.parol.set()
    if chat_id in  baza:
        kar = open("sticker.webm", "rb").read()
        await bot.send_sticker(chat_id, sticker=den)
        await message.answer("<b>Главное Меню !</b>", reply_markup=soglasie)



@dp.message_handler(state=akasil.parol)
async def gig(message: Message, state):
    kod = message.text
    chat_id = message.chat.id
    
    if kod == 'cicada':
        baza.append(message.chat.id)
        kar = open("sticker.webm", "rb").read()
        await message.answer("<b>Авторизация Подтвержденна</b>")
        time.sleep(3)
        await bot.send_sticker(chat_id, sticker=den)
        await message.answer('<b>Добро Пожаловать \nВ Управление Сайтом !\n\nmurmur48.cc</b>', reply_markup=soglasie)
        await state.finish()
    else:
        await message.answer("<b>Пароль Не Верен Отказанно В Доступе</b>")
        await state.finish()


@dp.callback_query_handler(text="mem")
async def mem(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await call.message.answer('<b>Добро Пожаловать \nВ Управление Сайтом !\n\nmurmur48.cc Меню главной страницы</b>', reply_markup=menuu)
    #await call.answer("Скоро Допишу Будет доступно")


@dp.callback_query_handler(text="moss")
async def moss(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await call.message.answer('<b>Добро Пожаловать \nВ Управление Сайтом !\n\nhttp://murmur48.cc МОСКВА</b>', reply_markup=menuu_mos)
    #await call.answer("Скоро Допишу Будет доступно")


@dp.callback_query_handler(text="piter")
async def piter(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await call.message.answer('<b>Добро Пожаловать \nВ Управление Сайтом !\n\nhttp://murmur48.cc САНКТ-ПЕТЕРБУРГ</b>', reply_markup=menuu_pit)


@dp.callback_query_handler(text="gig")
async def gig(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    gidra = open("gidra.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку Гидра Установлен\n"
        f"‼️ {gidra} ‼️\n\n"
        f":Для изменения контакта введите Новую ссылку\n\n"
    , reply_markup=otm)
    await akasil.oper.set()

@dp.message_handler(state=akasil.oper)
async def gig(message: Message, state):

    oper = message.text
    chat_id = message.chat.id
    

    with open("gidra.txt", "w", encoding="utf-8") as f:
        f.write(oper)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{oper}", reply_markup=soglasie)
    await state.finish()
        
@dp.callback_query_handler(text="su")
async def ssud(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    suda = open("suda.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку ➡️СЮДА⬅️ Установлен\n"
        f"‼️ {suda} ‼️\n\n"
        f":Для изменения контакта введите Новую ссылку\n\n"
    , reply_markup=otm)
    await akasil.wiwi.set()

@dp.message_handler(state=akasil.wiwi)
async def wiwi(message: Message, state):

    wiwi = message.text
    chat_id = message.chat.id
    

    with open("suda.txt", "w", encoding="utf-8") as f:
        f.write(wiwi)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{wiwi}", reply_markup=soglasie)
    await state.finish()

@dp.callback_query_handler(text="mmos")
async def name(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    name = open("mosscow.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку ➡️Москва⬅️ Установлен\n"
        f"‼️ {name} ‼️\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.name.set()

@dp.message_handler(state=akasil.name)
async def name(message: Message, state):

    name = message.text
    chat_id = message.chat.id
    

    with open("mosscow.txt", "w", encoding="utf-8") as f:
        f.write(name)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{name}", reply_markup=soglasie)
    await state.finish()

###############################

@dp.callback_query_handler(text="ppi")
async def oper2(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    oper2 = open("piter.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку ➡️Питер⬅️ Установлен\n"
        f"‼️ {oper2} ‼️\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.oper2.set()

@dp.message_handler(state=akasil.oper2)
async def oper2(message: Message, state):
    oper2 = message.text
    chat_id = message.chat.id
    

    oper2 = message.text
    chat_id = message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    with open("piter.txt", "w", encoding="utf-8") as f:
        f.write(oper2)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{oper2}", reply_markup=soglasie)
    await state.finish()
        

###############################
@dp.callback_query_handler(text="bbb2",  state='*')
async def tex(call: CallbackQuery, state: FSMContext):
    await state.finish()
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await call.message.answer("<b>Назад В Главное Меню</b>", reply_markup=soglasie)

@dp.callback_query_handler(text="bbb",  state='*')
async def tex(call: CallbackQuery, state: FSMContext):
    await state.finish()
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await call.message.answer("<b>Назад В Главное Меню</b>", reply_markup=soglasie)

@dp.callback_query_handler(text="bbb1",  state='*')
async def tex(call: CallbackQuery, state: FSMContext):
    await state.finish()
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await call.message.answer("<b>Назад В Главное Меню</b>", reply_markup=soglasie)
########################

@dp.callback_query_handler(text="vor")
async def tex(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    tex = open("voronej.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку ➡️Воронеж⬅️ Установлен\n"
        f"‼️ {tex} ‼️\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n", reply_markup=otm)
    await akasil.tex.set()

@dp.message_handler(state=akasil.tex)
async def tex(message: Message, state):
    tex = message.text
    
    chat_id = message.chat.id

    with open("voronej.txt", "w", encoding="utf-8") as f:
        f.write(tex)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{tex}", reply_markup=soglasie)
    await state.finish()
########################################

@dp.callback_query_handler(text="kupm")
async def tex2(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    tex2 = open("kupit.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку КУПИТЬ Установлен\n"
        f"‼️ {tex2} ‼️\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n", reply_markup=otm)
    await akasil.tex2.set()

@dp.message_handler(state=akasil.tex2)
async def tex(message: Message, state):
    tex2 = message.text
    
    chat_id = message.chat.id

    with open("kupit.txt", "w", encoding="utf-8") as f:
        f.write(tex2)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{tex2}", reply_markup=soglasie)
    await state.finish()

#################################

@dp.callback_query_handler(text="poddm")
async def bott(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    
    bott = open("poderM.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку поддержка Установлен\n"
        f"‼️ {bott} ‼️\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.bott.set()

@dp.message_handler(state=akasil.bott)
async def bott(message: Message, state):
    bott = message.text
    
    chat_id = message.chat.id

    with open("poderM.txt", "w", encoding="utf-8") as f:
        f.write(bott)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{bott}", reply_markup=soglasie)
    await state.finish()
############################

@dp.callback_query_handler(text="avm")
async def bott2(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    bott2 = open("autobotM.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку автобот Установлен\n"
        f"‼️ {bott2} ‼️\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.bott2.set()

@dp.message_handler(state=akasil.bott2)
async def bott2(message: Message, state):
    bott2 = message.text
    
    chat_id = message.chat.id

    with open("autobotM.txt", "w", encoding="utf-8") as f:
        f.write(bott2)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{bott2}", reply_markup=soglasie)
    await state.finish()


@dp.callback_query_handler(text="avm2")
async def forum(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    forum = open("aut2.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку автобот2 Установлен\n"
        f"‼️ {forum} ‼️\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.forum.set()

@dp.message_handler(state=akasil.forum)
async def forum(message: Message, state):
    forum = message.text
    
    chat_id = message.chat.id

    with open("aut2.txt", "w", encoding="utf-8") as f:
        f.write(forum)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{forum}", reply_markup=soglasie)
    await state.finish()


############################
###############################

@dp.callback_query_handler(text="wrkm")
async def forum2(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    
    forum2 = open("workM.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку РАБОТА Установлен\n"
        f"‼️ {forum2} ‼️\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.forum2.set()

@dp.message_handler(state=akasil.forum2)
async def forum(message: Message, state):
    forum2 = message.text
    chat_id = message.chat.id

    with open("workM.txt", "w", encoding="utf-8") as f:
        f.write(forum2)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{forum2}", reply_markup=soglasie)
    await state.finish()

##########################################################

@dp.callback_query_handler(text="kupp")
async def biz(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    
    biz = open("kupS.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку КУПИТЬ Установлен\n"
        f"‼️ {biz} ‼️ \n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.biz.set()

@dp.message_handler(state=akasil.biz)
async def biz(message: Message, state):
    biz = message.text
    
    chat_id = message.chat.id

    with open("kupS.txt", "w", encoding="utf-8") as f:
        f.write(biz)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{biz}", reply_markup=soglasie)
    await state.finish()

#############################

##########################################################

@dp.callback_query_handler(text="podp")
async def biz2(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    biz2 = open("poddS.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку поддержка Установлен\n"
        f"‼️ {biz2} ‼️\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.biz2.set()

@dp.message_handler(state=akasil.biz2)
async def biz2(message: Message, state):
    biz2 = message.text
    
    chat_id = message.chat.id

    with open("poddS.txt", "w", encoding="utf-8") as f:
        f.write(biz2)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{biz2}", reply_markup=soglasie)
    await state.finish()

#############################

@dp.callback_query_handler(text="avbp")
async def otziv(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    otziv = open("autbS.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку автобот Установлен\n"
        f"‼️ {otziv} ‼️\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.otziv.set()

@dp.message_handler(state=akasil.otziv)
async def otziv(message: Message, state):
    otziv = message.text
    
    chat_id = message.chat.id

    with open("autbS.txt", "w", encoding="utf-8") as f:
        f.write(otziv)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{otziv}", reply_markup=soglasie)
    await state.finish()


##################################################

#############################

@dp.callback_query_handler(text="avbp2")
async def otziv2(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    otziv2 = open("autb2S.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку автобот2 Установлен\n"
        f"‼️ {otziv2} ‼️\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.otziv2.set()

@dp.message_handler(state=akasil.otziv2)
async def otziv2(message: Message, state):
    otziv2 = message.text
    
    chat_id = message.chat.id

    with open("autb2S.txt", "w", encoding="utf-8") as f:
        f.write(otziv2)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{otziv2}", reply_markup=soglasie)
    await state.finish()

##################################################
@dp.callback_query_handler(text="wrkp")
async def bot2(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    bot2 = open("workS.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку РАБОТА Установлен\n"
        f"‼️ {bot2} ‼️\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.bot2.set()

@dp.message_handler(state=akasil.bot2)
async def bot2(message: Message, state):
    bot2 = message.text
    
    chat_id = message.chat.id

    with open("workS.txt", "w", encoding="utf-8") as f:
        f.write(bot2)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{bot2}", reply_markup=soglasie)
    await state.finish()


###################################

##################################################
@dp.callback_query_handler(text="wrkp")
async def bot22(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    bot22 = open("2/bot22.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку Работа Установлен\n"
        f"{bot22}\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.bot22.set()

@dp.message_handler(state=akasil.bot22)
async def bot22(message: Message, state):
    bot22 = message.text
    
    chat_id = message.chat.id

    with open("2/bot22.txt", "w", encoding="utf-8") as f:
        f.write(bot22)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{bot22}", reply_markup=soglasie)
    await state.finish()

###################################

@dp.callback_query_handler(text="img2")
async def img1(call: CallbackQuery):
    ch = call.message.chat.id
    izob = open("img1.jpg", "rb").read()

    cap = (
        f"Сейчас Установлен Логотип\n"
        f":Для изменения Логотипа Отправь Мне Картинку\n\n"
    )
    await bot.send_photo(chat_id=ch, photo=izob, caption=cap, reply_markup=otm)
    await akasil.img1.set()

@dp.message_handler(state=akasil.img1, content_types=types.ContentTypes.ANY)
async def img1(message: Message, state: FSMContext):
    ch = message.chat.id
    img1 = message.photo[-1]
    
    photo_name = "img1.jpg"
    await message.photo[-1].download(f"{photo_name}")
    link = await upload_document(message.bot, img1)
    with open("img1.txt", "w", encoding="utf-8") as f:
        f.write(link)
    await state.finish()
    izob = open("img1.jpg", "rb").read()
    ca = (f"Логотип Изменен  \n")
    mur()
    await bot.send_photo(chat_id=ch, photo=izob, caption=ca, reply_markup=soglasie)

####################################
###################################

@dp.callback_query_handler(text="img22")
async def img22(call: CallbackQuery):
    ch = call.message.chat.id
    izob = open("2/img22.jpg", "rb").read()

    cap = (
        f"Сейчас Установлен Логотип\n"
        f":Для изменения Логотипа Отправь Мне Картинку\n\n"
    )
    await bot.send_photo(chat_id=ch, photo=izob, caption=cap, reply_markup=otm)
    await akasil.img22.set()

@dp.message_handler(state=akasil.img22, content_types=types.ContentTypes.ANY)
async def img22(message: Message, state: FSMContext):
    ch = message.chat.id
    img22 = message.photo[-1]
    
    photo_name = "img22.jpg"
    await message.photo[-1].download(f"2/{photo_name}")
    link = await upload_document(message.bot, img22)
    with open("2/img22.txt", "w", encoding="utf-8") as f:
        f.write(link)
    await state.finish()
    izob = open("2/img22.jpg", "rb").read()
    ca = (f"Логотип Изменен  \n")
    mur()
    await bot.send_photo(chat_id=ch, photo=izob, caption=ca, reply_markup=soglasie)

####################################

@dp.callback_query_handler(text="img1")
async def img2(call: CallbackQuery):
    ch = call.message.chat.id
    izob = open("img2.jpg", "rb").read()

    cap = (
        f"Сейчас Установлен Фон\n"
        f":Для изменения Фона Отправь Мне Картинку\n\n"
    )
    await bot.send_photo(chat_id=ch, photo=izob, caption=cap, reply_markup=otm)
    await akasil.img2.set()

@dp.message_handler(state=akasil.img2, content_types=types.ContentTypes.ANY)
async def img2(message: Message, state: FSMContext):
    ch = message.chat.id
    img2 = message.photo[-1]
    
    photo_name = "img2.jpg"
    await message.photo[-1].download(f"{photo_name}")
    link = await upload_document(message.bot, img2)
    with open("img2.txt", "w", encoding="utf-8") as f:
        f.write(link)
    await state.finish()
    izob = open("img2.jpg", "rb").read()
    ca = (f"Фон Изменен  \n")
    mur()
    await bot.send_photo(chat_id=ch, photo=izob, caption=ca, reply_markup=soglasie)

####################################

@dp.callback_query_handler(text="img12")
async def img12(call: CallbackQuery):
    ch = call.message.chat.id
    izob = open("2/img12.jpg", "rb").read()

    cap = (
        f"Сейчас Установлен Фон\n"
        f":Для изменения Фона Отправь Мне Картинку\n\n"
    )
    await bot.send_photo(chat_id=ch, photo=izob, caption=cap, reply_markup=otm)
    await akasil.img12.set()

@dp.message_handler(state=akasil.img12, content_types=types.ContentTypes.ANY)
async def img12(message: Message, state: FSMContext):
    ch = message.chat.id
    img12 = message.photo[-1]
    
    photo_name = "img12.jpg"
    await message.photo[-1].download(f"2/{photo_name}")
    link = await upload_document(message.bot, img12)
    with open("2/img12.txt", "w", encoding="utf-8") as f:
        f.write(link)
    await state.finish()
    izob = open("2/img12.jpg", "rb").read()
    ca = (f"Фон Изменен  \n")
    mur()
    await bot.send_photo(chat_id=ch, photo=izob, caption=ca, reply_markup=soglasie)





















@dp.callback_query_handler(text="ss")
async def ss(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    ss = open("3/rb.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку Работа Установлен\n"
        f"‼️ {ss} ‼️\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm3)
    await akasil.ss.set()

@dp.message_handler(state=akasil.ss)
async def gig(message: Message, state):
    ss = message.text
    chat_id = message.chat.id
    

    with open("3/rb.txt", "w", encoding="utf-8") as f:
        f.write(ss)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{ss}", reply_markup=soglasie3)
    await state.finish()


########################

@dp.callback_query_handler(text="zzz")
async def tex(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    zzz = open("3/suda.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку ➡️СЮДА⬅️ Установлен\n"
        f"{zzz}\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n", reply_markup=otm3)
    await akasil.zzz.set()

@dp.message_handler(state=akasil.zzz)
async def zzz(message: Message, state):
    zzz = message.text
    
    chat_id = message.chat.id

    with open("3/suda.txt", "w", encoding="utf-8") as f:
        f.write(zzz)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{zzz}", reply_markup=soglasie3)
    await state.finish()


@dp.callback_query_handler(text="bzbz")
async def bzbz(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    bzbz = open("3/biz.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку Biz Установлен\n"
        f"{bzbz}\n\n"
        f":Для изменения контакта введите адрес сайта\n\n"
    , reply_markup=otm3)
    await akasil.bzbz.set()

@dp.message_handler(state=akasil.bzbz)
async def bzbz(message: Message, state):
    bzbz = message.text
    chat_id = message.chat.id
    

    with open("3/biz.txt", "w", encoding="utf-8") as f:
        f.write(bzbz)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{bzbz}", reply_markup=soglasie3)
    await state.finish()


@dp.callback_query_handler(text="ffff")
async def ffff(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    ffff = open("3/sha.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас  Текст Шапки Установлен\n"
        f"{ffff}\n\n"
        f":Для изменения Шапки введите Новый Текст\n\n"
    , reply_markup=otm3)
    await akasil.ffff.set()

@dp.message_handler(state=akasil.ffff)
async def ffff(message: Message, state):
    ffff = message.text
    
    chat_id = message.chat.id

    with open("3/sha.txt", "w", encoding="utf-8") as f:
        f.write(ffff)
    await state.finish()
    mur()
    await message.answer(f"Контакт Изменен на:  \n"
                        f"{ffff}", reply_markup=soglasie3)
    await state.finish()


@dp.callback_query_handler(text="mzmz")
async def mzmz(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    mzmz = open("3/ser.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас Текст Основ. Установлен\n"
        f"{mzmz}\n\n"
        f":Для изменения Введи Новый Текст\n\n"
    , reply_markup=otm3)
    await akasil.mzmz.set()

@dp.message_handler(state=akasil.mzmz)
async def mzmz(message: Message, state):
    mzmz = message.text
    
    chat_id = message.chat.id

    with open("3/ser.txt", "w", encoding="utf-8") as f:
        f.write(mzmz)
    await state.finish()
    mur()
    await message.answer(f"Изменен на:  \n"
                        f"{mzmz}", reply_markup=soglasie3)
    await state.finish()


#############################


@dp.callback_query_handler(text="img13")
async def img2(call: CallbackQuery):
    ch = call.message.chat.id
    izob3 = open("3/img2.jpg", "rb").read()

    cap = (
        f"Сейчас Установлен Фон\n"
        f":Для изменения Фона Отправь Мне Картинку\n\n"
    )
    await bot.send_photo(chat_id=ch, photo=izob3, caption=cap, reply_markup=otm3)
    await akasil.izob3.set()

@dp.message_handler(state=akasil.izob3, content_types=types.ContentTypes.ANY)
async def img2(message: Message, state: FSMContext):
    ch = message.chat.id
    izob3 = message.photo[-1]
    photo_name = "img2.jpg"
    await message.photo[-1].download(f"3/{photo_name}")
    
    link = await upload_document(message.bot, izob3)
    with open("3/fon.txt", "w", encoding="utf-8") as f:
        f.write(link)
    await state.finish()
    izob3 = open("3/img2.jpg", "rb").read()
    ca = (f"Фон Изменен  \n")
    mur()
    await bot.send_photo(chat_id=ch, photo=izob3, caption=ca, reply_markup=soglasie3)







if __name__ == '__main__':
    executor.start_polling(dp)