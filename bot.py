import logging
import sqlite3
import telebot

from telegram import *
from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from buttons import keyboard1, keyboard2, keyboard3, keyboard4, keyboard5, keyboard6, keyboard7, keyboard8, keyboard9, keyboard10, keyboard11, keyboard12, keyboard13



API_TOKEN = '6694811561:AAEdvNV_MCvraAjDObaM-bEsbxhwRdAnm3w'

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, proxy=None, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
 

# Bosh menyu klaviaturasi
keyboard_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu_buttons = ["Start", "Help", "About", "Settings"]
keyboard_main.add(*menu_buttons)
 
@dp.message_handler(commands=["random"])
async def random_value(message: types.Message):
    await message.answer("Iltimos, tugmalardan birini bosing!", reply_markup=keyboard2)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user = message.from_user
    full_name = user.first_name
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        button_1 TEXT,
        button_2 TEXT,
        button_3 TEXT,
        button_4 TEXT,
        button_5 TEXT,
        button_6 TEXT,
        button_7 TEXT,
        button_8 TEXT,
        button_9 TEXT,
        button_10 TEXT,
        button_11 TEXT,
        button_12 TEXT,
        button_13 TEXT,
        button_14 TEXT,
        button_15 TEXT,
        button_16 TEXT,
        button_17 TEXT,
        button_18 TEXT,
        button_19 TEXT,
        button_20 TEXT
    )''')
    
    connect.commit()
    
    user_id = message.from_user.id
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}") 
    result = cursor.fetchone()
    if result is None:
        # user_data = (user_id, user.username, user.first_name, user.last_name, None)
        user_data = (user_id, user.username, user.first_name, user.last_name, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", user_data)
        connect.commit()
            
        # Foydalanuvchiga xush kelibsiz xabarini yuborish
        await message.answer(f"Assalomu alaykum, {full_name}!!!  \n Botimizga xush kelibsiz.", reply_markup=keyboard1)
    else:
        await message.answer("Siz allaqachon botni ishlatgansiz!!!", reply_markup=keyboard1)

    print(message.from_user.id)
    print(message.from_user.first_name)
    print(message.from_user.last_name)
    print(message.from_user.username)
    print(message.from_user.full_name)
    

@dp.message_handler(lambda message: message.text in menu_buttons)
async def handle_menu(message: types.Message):
    selected_menu = message.text.lower()  # Foydalanuvchi tanlagan menyuni olish
    
    if selected_menu == "start":
        await message.answer("Siz Start menyusini tanladingiz.")
    elif selected_menu == "help":
        await message.answer("Siz Help menyusini tanladingiz.")
    elif selected_menu == "about":
        await message.answer("Siz About menyusini tanladingiz.")
    elif selected_menu == "settings":
        await message.answer("Siz Settings menyusini tanladingiz.")


@dp.message_handler()
async def kb_answer(message: types.Message):
    
    if message.text == "🇺🇿 O\'zbekcha":
        await message.answer("Sizga qanday yordam bera olaman?", reply_markup=keyboard2)
    elif message.text == "🇷🇺 Русский":
        await message.answer("Как я могу вам помочь?", reply_markup=keyboard3)
    elif message.text == "🇬🇧 English":
        await message.answer("How can I help you?", reply_markup=keyboard4)
    else:
        await message.answer("Iltimos, tugmalardan birini bosing!", reply_markup=keyboard2) 
        
        
 
@dp.callback_query_handler(text=["maqola", "dgu", "sertifikat"])       
async def random_value_1(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "maqola":
        text = "Maqola"
    elif call.data == "dgu":
        text = "DGU"
    elif call.data == "sertifikat":
        text = "Sertifikat"
    
    cursor.execute("UPDATE users SET button_1 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    await call.message.answer("Qaysi birini tanlaysiz?", reply_markup=keyboard5)
    
    # if call.data == "maqola":
    #     await call.message.answer("Qaysi birini tanlaysiz?", reply_markup=keyboard5)
    # elif call.data == "dgu":
    #     await call.message.answer("DGU")
    # elif call.data == "sertifikat":
    #     await call.message.answer("Sertifikat", reply_markup=keyboard11)
    # else:
    #     await call.message.answer("Iltimos, tugmalardan birini bosing!", reply_markup=keyboard2)
        
        
@dp.callback_query_handler(text=["Статья", "ДГУ", "Сертификат"])       
async def random_value_2(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "Статья":
        text = "Maqola"
    elif call.data == "ДГУ":
        text = "DGU"
    elif call.data == "Сертификат":
        text = "Sertifikat"
    
    cursor.execute("UPDATE users SET button_1 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    await call.message.answer("Qaysi birini tanlaysiz?", reply_markup=keyboard6)
    
    # if call.data == "Статья":
    #     await call.message.answer("Какой из них вы выберете?", reply_markup=keyboard6)
    # elif call.data == "ДГУ":
    #     await call.message.answer("ДГУ")
    # elif call.data == "Сертификат":
    #     await call.message.answer("Сертификат", reply_markup=keyboard12)
    # else:
    #     await call.message.answer("Пожалуйста, нажмите одну из кнопок!", reply_markup=keyboard2)
        
        

@dp.callback_query_handler(text=["article", "patent", "certificate"])       
async def random_value_3(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "article":
        text = "Article"
    elif call.data == "patent":
        text = "DGU"
    elif call.data == "certificate":
        text = "Certificate"
    
    cursor.execute("UPDATE users SET button_1 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    await call.message.answer("Qaysi birini tanlaysiz?", reply_markup=keyboard7)
    
    # if call.data == "article":
    #     await call.message.answer("Which one will you choose?", reply_markup=keyboard7)
    # elif call.data == "patent":
    #     await call.message.answer("DGU")
    # elif call.data == "certificate":
    #     await call.message.answer("Certificate", reply_markup=keyboard13)
    # else:
    #     await call.message.answer("Please press one of the buttons!", reply_markup=keyboard2)
        

executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    print("Starting bot...")
 