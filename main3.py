import requests
from test import sborka
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
from klava import menu3, izm3, domenu3,  otm3
from string import ascii_letters, digits
import logging 
token = "2009993885:AAEdYrlNFdlyfSx93q1nSKb5HWN13W3pm1o"
bot = Bot(token=token,parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

#
#oper = open("3/rb.txt", "a", encoding="utf-8").read()
#tex = open("3/suda.txt", "a", encoding="utf-8").read()
#izob = open("3/fon.txt", "a", encoding="utf-8").read()
#bott = open("3/biz.txt", "a", encoding="utf-8").read()
#forum = open("3/sha.txt", "a", encoding="utf-8").read()
#biz = open("3/ser.txt", "a", encoding="utf-8").read()
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
    forum = State()
    bott = State()
    tex = State()
    oper = State()
    img1 = State()
    img2 = State()
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
        kar = open("3/sticker.webm", "rb").read()
        await bot.send_sticker(chat_id, sticker=den)
        await message.answer("<b>Главное Меню !</b>", reply_markup=menu3)



@dp.message_handler(state=akasil.parol)
async def gig(message: Message, state):
    kod = message.text
    chat_id = message.chat.id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    if kod == 'cicada':
        baza.append(message.chat.id)
        kar = open("3/sticker.webm", "rb").read()
        await message.answer("<b>Авторизация Подтвержденна</b>")
        time.sleep(3)
        await bot.send_sticker(chat_id, sticker=den)
        await message.answer('<b>Добро Пожаловать \nВ Управление Сайтом !</b>', reply_markup=domenu3)
        await state.finish()
    else:
        await message.answer("<b>Пароль Не Верен Отказанно В Доступе</b>")
        await state.finish()


@dp.callback_query_handler(text="cj2")
async def cj1(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await call.message.answer('<b>Добро Пожаловать \nВ Управление Сайтом !</b>', reply_markup=menu3)
    #await call.answer("Скоро Допишу Будет доступно")


@dp.callback_query_handler(text="cj1")
async def cj2(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await call.message.answer('<b>Добро Пожаловать \nВ Управление Сайтом !</b>', reply_markup=menu3)
    #await call.answer("Скоро Допишу Будет доступно")



@dp.callback_query_handler(text="rabota")
async def oper(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    oper = open("3/rb.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку Работа Установлен\n"
        f"‼️ {oper} ‼️\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.oper.set()

@dp.message_handler(state=akasil.oper)
async def gig(message: Message, state):
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    oper = message.text
    chat_id = message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await message.answer(f"<b>Принять Изменения Контаута \nНа {oper} ?</b>", reply_markup=izm)
    @dp.callback_query_handler(state=akasil.oper, text="yes")
    async def oper(call: CallbackQuery, state):
        oper = message.text
        chat_id = message.chat.id
        await bot.send_sticker(chat_id, sticker=st)
        with open("3/rb.txt", "w", encoding="utf-8") as f:
            f.write(oper)
        await state.finish()
        sborka()
        await message.answer(f"Контакт Изменен на:  \n"
                            f"{oper}", reply_markup=menu3)
        await state.finish()
        
    @dp.callback_query_handler(state=akasil.oper, text="no")
    async def oper(call: CallbackQuery, state):
        chat_id = message.chat.id
        await bot.send_sticker(chat_id, sticker=st)
        await call.answer("Изменения Отменены")
        await call.message.answer("<b>Изменения Отменены</b>", reply_markup=menu3)
        await state.finish()
###############################
@dp.callback_query_handler(text="bbb2",  state='*')
async def tex(call: CallbackQuery, state: FSMContext):
    await state.finish()
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await call.message.answer("<b>Назад В Главное Меню</b>", reply_markup=menu32)

@dp.callback_query_handler(text="bbb",  state='*')
async def tex(call: CallbackQuery, state: FSMContext):
    await state.finish()
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await call.message.answer("<b>Назад В Главное Меню</b>", reply_markup=menu3)

@dp.callback_query_handler(text="bbb1",  state='*')
async def tex(call: CallbackQuery, state: FSMContext):
    await state.finish()
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await call.message.answer("<b>Назад В Главное Меню</b>", reply_markup=domenu3)
########################

@dp.callback_query_handler(text="tex")
async def tex(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    tex = open("3/suda.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку ➡️СЮДА⬅️ Установлен\n"
        f"{tex}\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n", reply_markup=otm)
    await akasil.tex.set()

@dp.message_handler(state=akasil.tex)
async def tex(message: Message, state):
    tex = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    chat_id = message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await message.answer(f"<b>Принять Изменения Контаута \nНа {tex} ?</b>", reply_markup=izm)
    @dp.callback_query_handler(state=akasil.tex, text="yes")
    async def tex(call: CallbackQuery, state):
        tex = message.text
        chat_id = call.message.chat.id
        await bot.send_sticker(chat_id, sticker=st)
        with open("3/suda.txt", "w", encoding="utf-8") as f:
            f.write(tex)
        await state.finish()
        sborka()
        await message.answer(f"Контакт Изменен на:  \n"
                            f"{tex}", reply_markup=menu3)
        await state.finish()
    @dp.callback_query_handler(state=akasil.tex, text="no")
    async def tex(call: CallbackQuery, state):
        chat_id = call.message.chat.id
        await bot.send_sticker(chat_id, sticker=st)
        await call.answer("Изменения Отменены")
        await call.message.answer("<b>Изменения Отменены</b>", reply_markup=menu3)
        await state.finish()

@dp.callback_query_handler(text="bott")
async def bott(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    bott = open("3/biz.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку Biz Установлен\n"
        f"{bott}\n\n"
        f":Для изменения контакта введите адрес сайта\n\n"
    , reply_markup=otm)
    await akasil.bott.set()

@dp.message_handler(state=akasil.bott)
async def bott(message: Message, state):
    bott = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    chat_id = message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await message.answer(f"<b>Принять Изменения Контаута \nНа {bott} ?</b>", reply_markup=izm)
    @dp.callback_query_handler(state=akasil.bott, text="yes")
    async def bott(call: CallbackQuery, state):
        bott = message.text
        chat_id = call.message.chat.id
        await bot.send_sticker(chat_id, sticker=st)
        with open("3/biz.txt", "w", encoding="utf-8") as f:
            f.write(bott)
        await state.finish()
        sborka()
        await message.answer(f"Контакт Изменен на:  \n"
                            f"{bott}", reply_markup=menu3)
        await state.finish()
    @dp.callback_query_handler(state=akasil.bott, text="no")
    async def bott(call: CallbackQuery, state):
        chat_id = call.message.chat.id
        await bot.send_sticker(chat_id, sticker=st)
        await call.answer("Изменения Отменены")
        await call.message.answer("<b>Изменения Отменены</b>", reply_markup=menu3)
        await state.finish()

@dp.callback_query_handler(text="forum")
async def forum(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    forum = open("3/sha.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас  Текст Шапки Установлен\n"
        f"{forum}\n\n"
        f":Для изменения Шапки введите Новый Текст\n\n"
    , reply_markup=otm)
    await akasil.forum.set()

@dp.message_handler(state=akasil.forum)
async def forum(message: Message, state):
    forum = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    chat_id = message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await message.answer(f"<b>Принять Изменения  \nНа {forum} ?</b>", reply_markup=izm)
    @dp.callback_query_handler(state=akasil.forum, text="yes")
    async def forum(call: CallbackQuery, state):
        forum = message.text
        chat_id = call.message.chat.id
        await bot.send_sticker(chat_id, sticker=st)
        with open("3/sha.txt", "w", encoding="utf-8") as f:
            f.write(forum)
        await state.finish()
        sborka()
        await message.answer(f"Контакт Изменен на:  \n"
                            f"{forum}", reply_markup=menu3)
        await state.finish()
    @dp.callback_query_handler(state=akasil.forum, text="no")
    async def forum(call: CallbackQuery, state):
        chat_id = call.message.chat.id
        await bot.send_sticker(chat_id, sticker=st)
        await call.answer("Изменения Отменены")
        await call.message.answer("<b>Изменения Отменены</b>", reply_markup=menu3)
        await state.finish()

@dp.callback_query_handler(text="biz")
async def biz(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    biz = open("3/ser.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас Текст Основ. Установлен\n"
        f"{biz}\n\n"
        f":Для изменения Введи Новый Текст\n\n"
    , reply_markup=otm)
    await akasil.biz.set()

@dp.message_handler(state=akasil.biz)
async def biz(message: Message, state):
    biz = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    chat_id = message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await message.answer(f"<b>Принять Изменения \nНа {biz} ?</b>", reply_markup=izm)
    @dp.callback_query_handler(state=akasil.biz, text="yes")
    async def biz(call: CallbackQuery, state):
        biz = message.text
        chat_id = call.message.chat.id
        await bot.send_sticker(chat_id, sticker=st)
        with open("3/ser.txt", "w", encoding="utf-8") as f:
            f.write(biz)
        await state.finish()
        sborka()
        await message.answer(f"Изменен на:  \n"
                            f"{biz}", reply_markup=menu3)
        await state.finish()
    @dp.callback_query_handler(state=akasil.biz, text="no")
    async def biz(call: CallbackQuery, state):
        chat_id = call.message.chat.id
        await bot.send_sticker(chat_id, sticker=st)
        await call.answer("Изменения Отменены")
        await call.message.answer("<b>Изменения Отменены</b>", reply_markup=menu3)
        await state.finish()

#############################
\
@dp.callback_query_handler(text="otziv")
async def otziv(call: CallbackQuery):
    chat_id = call.message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    otziv = open("3/otziv.txt", "r", encoding="utf-8").read()
    await call.message.answer(
        f"Сейчас на Кнопку ОТЗЫВЫ Установлен\n"
        f"{otziv}\n\n"
        f":Для изменения контакта введите Username \nбез ⚠️  http://t.me/ ⚠️ и без ⚠️ @ ⚠️\n\n"
    , reply_markup=otm)
    await akasil.otziv.set()

@dp.message_handler(state=akasil.otziv)
async def otziv(message: Message, state):
    otziv = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    chat_id = message.chat.id
    await bot.send_sticker(chat_id, sticker=st)
    await message.answer(f"<b>Принять Изменения Контаута \nНа {otziv} ?</b>", reply_markup=izm)
    @dp.callback_query_handler(state=akasil.otziv, text="yes")
    async def otziv(call: CallbackQuery, state):
        otziv = message.text
        chat_id = call.message.chat.id
        await bot.send_sticker(chat_id, sticker=st)
        with open("3/otziv.txt", "w", encoding="utf-8") as f:
            f.write(otziv)
        await state.finish()
        sborka()
        await message.answer(f"Контакт Изменен на:  \n"
                            f"{otziv}", reply_markup=menu3)
        await state.finish()
    @dp.callback_query_handler(state=akasil.otziv, text="no")
    async def otziv(call: CallbackQuery, state):
        chat_id = call.message.chat.id
        await bot.send_sticker(chat_id, sticker=st)
        await call.answer("Изменения Отменены")
        await call.message.answer("<b>Изменения Отменены</b>", reply_markup=menu3)
        await state.finish()


@dp.callback_query_handler(text="img1")
async def img2(call: CallbackQuery):
    ch = call.message.chat.id
    izob = open("3/img2.jpg", "rb").read()

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
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    photo_name = "img2.jpg"
    await message.photo[-1].download(f"{photo_name}")
    link = await upload_document(message.bot, img2)
    with open("3/fon.txt", "w", encoding="utf-8") as f:
        f.write(link)
    await state.finish()
    izob = open("3/img2.jpg", "rb").read()
    ca = (f"Фон Изменен  \n")
    sborka()
    await bot.send_photo(chat_id=ch, photo=izob, caption=ca, reply_markup=menu3)

if __name__ == '__main__':
    executor.start_polling(dp)
