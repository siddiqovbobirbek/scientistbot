import logging
import sqlite3
import telebot, os

from telegram import *
from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from buttons import keyboard1, keyboard2, keyboard3, keyboard4, keyboard5, keyboard6, keyboard7, keyboard8, keyboard9, keyboard10, keyboard11, keyboard12, keyboard13, keyboard14, keyboard15, keyboard16
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InputFile
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # Storage ni import qilamiz
from aiogram.utils import executor
from enum import Enum


# Foydalanuvchi holatlari uchun ENUM
class UserStates(StatesGroup):
    waiting_for_file = State()  # Faylni yuklash holati
    waiting_for_agreement = State()  # Shartnoma qabul qilish holati


UPLOADS_DIR = "uploads"  # Fayllarni saqlash uchun papka nomi
os.makedirs(UPLOADS_DIR, exist_ok=True)


API_TOKEN = '6694811561:AAEdvNV_MCvraAjDObaM-bEsbxhwRdAnm3w'

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, proxy=None, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()  # Storage yaratamiz
dp = Dispatcher(bot, storage=storage)
 

# Bosh menyu klaviaturasi
keyboard_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu_buttons = ["Start", "Help", "About", "Settings"]
keyboard_main.add(*menu_buttons)
 
@dp.message_handler(commands=["random"])
async def random_value(message: types.Message):
    await message.answer("Iltimos, tugmalardan birini bosing!", reply_markup=keyboard2)



@dp.message_handler(commands=['shartnomani_olish'])
async def get_agreement(message: types.Message):
    agreement_path = "shartnoma.pdf"  # Shartnoma faylini joylash manzili
    with open(agreement_path, 'rb') as agreement_file:
        await bot.send_document(message.chat.id, agreement_file)

    # "Tushundim" degan buttonni yaratish
    button = types.InlineKeyboardButton(text="Tushundim", callback_data="agreement_accepted")
    shart = types.InlineKeyboardMarkup().add(button)
    
    await message.reply("Shartnomani o'qib chiqib, rozilik bildiring:", reply_markup=shart)

@dp.callback_query_handler(lambda call: call.data == "agreement_accepted")
async def agreement_accepted(call: types.CallbackQuery):
    # Foydalanuvchi rozilik bildirdi, shu yerdan davom etishingiz mumkin
    await bot.answer_callback_query(call.id, text="Rozilik bildirganingiz uchun rahmat!")
 # Foydalanuvchilar yuklab olayotgan faylni shartnomaga bog'liqligini tekshirish uchun lug'at
   
   
   
# @dp.message_handler(content_types=types.ContentTypes.DOCUMENT, state=UserStates.waiting_for_file)
# async def upload_file(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['file'] = message.document.file_id
#         data['user_id'] = message.from_user.id
        
#     await UserStates.waiting_for_agreement.set()
    
#     agreement_button = types.InlineKeyboardButton("Rozilik", callback_data="rozilik")
#     keyboard = types.InlineKeyboardMarkup().add(agreement_button)
#     await message.answer("Siz fayl muvaffaqiyatli yukladingiz. Hozir shartnoma qabul qilishingiz mumkin.", reply_markup=keyboard)



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
        await call.message.answer("Qaysi birini tanlaysiz?", reply_markup=keyboard5)
        text = "Maqola"
    elif call.data == "dgu":
        await call.message.answer("DGU")
        text = "DGU"
    elif call.data == "sertifikat":
        await call.message.answer("Sertifikat", reply_markup=keyboard11)
        text = "Sertifikat"
    else:
        await call.message.answer("Iltimos, tugmalardan birini bosing!", reply_markup=keyboard2)
     
    cursor.execute("UPDATE users SET button_1 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()   
    
        
        
@dp.callback_query_handler(text=["Статья", "ДГУ", "Сертификат"])       
async def random_value_2(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
        
    if call.data == "Статья":
        await call.message.answer("Какой из них вы выберете?", reply_markup=keyboard6)
        text = "Статья"
    elif call.data == "ДГУ":
        await call.message.answer("ДГУ")
        text = "ДГУ"
    elif call.data == "Сертификат":
        await call.message.answer("Сертификат", reply_markup=keyboard12)
        text = "Сертификат"
    else:
        await call.message.answer("Пожалуйста, нажмите одну из кнопок!", reply_markup=keyboard2)
        
    cursor.execute("UPDATE users SET button_1 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
        

@dp.callback_query_handler(text=["article", "patent", "certificate"])       
async def random_value_3(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
        
    if call.data == "article":
        await call.message.answer("Which one will you choose?", reply_markup=keyboard7)
        text = "Article"
    elif call.data == "patent":
        await call.message.answer("DGU")
        text = "Patent"
    elif call.data == "certificate":
        await call.message.answer("Certificate", reply_markup=keyboard13)
        text = "Certificate"
    else:
        await call.message.answer("Please press one of the buttons!", reply_markup=keyboard2)
        
    cursor.execute("UPDATE users SET button_1 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    

    
@dp.callback_query_handler(text=["maqola_1", "maqola_2", "maqola_3", "maqola_4"])
async def maqola_yozish(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor() 
    user_id = call.from_user.id
    text = ""
    
    if call.data == "maqola_1":
        await call.message.answer("OAK uchun", reply_markup=keyboard8)
        text = "OAK uchun"
    elif call.data == "maqola_2":
        await call.message.answer("Respublika konferensiya uchun", reply_markup=keyboard8)
        text = "Respublika konferensiya uchun"
    elif call.data == "maqola_3":
        await call.message.answer("Xalqaro ilmiy jurnal uchun", reply_markup=keyboard8)
        text = "Xalqaro ilmiy jurnal uchun"
    elif call.data == "maqola_4":
        await call.message.answer("Xalqaro konferensiya uchun", reply_markup=keyboard8)
        text = "Xalqaro konferensiya uchun"
    else:
        await call.message.answer("Iltimos, tugmalardan birini bosing!", reply_markup=keyboard2)

    
    cursor.execute("UPDATE users SET button_2 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    
@dp.callback_query_handler(text=["cтатья_1", "cтатья_2", "cтатья_3", "cтатья_4"])
async def написать_статью(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "cтатья_1":
        await call.message.answer("Для OAC", reply_markup=keyboard9)
        text = "Для OAC"
    elif call.data == "cтатья_2":
        await call.message.answer("Для республиканской конференции", reply_markup=keyboard9)
        text = "Для республиканской конференции"
    elif call.data == "cтатья_3":
        await call.message.answer("Для международного научного журнала", reply_markup=keyboard9)
        text = "Для международного научного журнала"
    elif call.data == "cтатья_4":
        await call.message.answer("Для международной конференции", reply_markup=keyboard9)
        text = "Для международной конференции"
    else:
        await call.message.answer("Пожалуйста, нажмите одну из кнопок!", reply_markup=keyboard2)
        
    cursor.execute("UPDATE users SET button_2 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()    
        
        
@dp.callback_query_handler(text=["article_1", "article_2", "article_3", "article_4"])
async def write_article(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "article_1":
        await call.message.answer("For OAC", reply_markup=keyboard10)
        text = "For OAC"
    elif call.data == "article_2":
        await call.message.answer("For the Republican Conference", reply_markup=keyboard10)
        text = "For the Republican Conference"
    elif call.data == "article_3":
        await call.message.answer("For an international scientific journal", reply_markup=keyboard10)
        text = "For an international scientific journal"
    elif call.data == "article_4":
        await call.message.answer("For an international conference", reply_markup=keyboard10)
        text = "For an international conference"
    else:
        await call.message.answer("Please press one of the buttons!", reply_markup=keyboard2)
    
    cursor.execute("UPDATE users SET button_2 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()    
    
    
@dp.callback_query_handler(text=["yozish", "yozish_chop_etish", "chop_etish"])
async def yozish_chop_etish(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "yozish":
        await call.message.answer("Yozib berish!", reply_markup=keyboard14)
        text = "Yozib berish!"
    elif call.data == "yozish_chop_etish":
        await call.message.answer("Yozib berish va chop etish!", reply_markup=keyboard14)
        text = "Yozib berish va chop etish!"
    elif call.data == "chop_etish":
        await call.message.answer("Tayyor maqolani chop etish!", reply_markup=upload_file)
        await call.message.answer("Tayyor maqolani chop etish!", reply_markup=keyboard14)

        text = "Tayyor maqolani chop etish!"
    else:
        await call.message.answer("Iltimos, tugmalardan birini bosing!", reply_markup=keyboard2)
    
    cursor.execute("UPDATE users SET button_4 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    

    
@dp.callback_query_handler(text=["написать", "написать_распечатать", "распечатать"])
async def написать_распечатать(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "написать":
        await call.message.answer("Написать!", reply_markup=keyboard15)
        text = "Написать!"
    elif call.data == "написать_распечатать":
        await call.message.answer("Написать и распечатать!", reply_markup=keyboard15)
        text = "Написать и распечатать!"
    elif call.data == "распечатать":
        await call.message.answer("Распечатать готовую статью!", reply_markup=keyboard15)
        text = "Распечатать готовую статью!"
    else:
        await call.message.answer("Пожалуйста, нажмите одну из кнопок!", reply_markup=keyboard2)
    
    cursor.execute("UPDATE users SET button_4 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    
@dp.callback_query_handler(text=["write", "write_print", "print"])
async def write_print(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "write":
        await call.message.answer("Write!", reply_markup=keyboard16)
        text = "Write!"
    elif call.data == "write_print":
        await call.message.answer("Write and print!", reply_markup=keyboard16)
        text = "Write and print!"
    elif call.data == "print":
        await call.message.answer("Print a finished article!", reply_markup=keyboard16)
        text = "Print a finished article!"
    else:
        await call.message.answer("Please press one of the buttons!", reply_markup=keyboard2)
    
    cursor.execute("UPDATE users SET button_4 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    
    
@dp.callback_query_handler(text=["texnika", "iqtisodiyot", "tibbiyot", "pedagogika"])
async def sohalar(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "texnika":
        await call.message.answer("Texnika")
        text = "Texnika"
    elif call.data == "iqtisodiyot":
        await call.message.answer("Iqtisodiyot")
        text = "Iqtisodiyot"
    elif call.data == "tibbiyot":
        await call.message.answer("Tibbiyot")
        text = "Tibbiyot"
    elif call.data == "pedagogika":
        await call.message.answer("Pedagogika")
        text = "Pedagogika"
    else:
        await call.message.answer("Iltimos, tugmalardan birini bosing!", reply_markup=keyboard2)
    
    cursor.execute("UPDATE users SET button_5 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    
@dp.callback_query_handler(text=["техника", "экономика", "медицина", "педагогика"])
async def направления(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""

    if call.data == "техника":
        await call.message.answer("Техника")
        text = "Техника"
    elif call.data == "экономика":
        await call.message.answer("Экономика")
        text = "Экономика"
    elif call.data == "медицина":
        await call.message.answer("Медицина")
        text = "Медицина"
    elif call.data == "педагогика":
        await call.message.answer("Педагогика")
        text = "Педагогика"
    else:
        await call.message.answer("Пожалуйста, нажмите одну из кнопок!", reply_markup=keyboard2)
    
    cursor.execute("UPDATE users SET button_5 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    

@dp.callback_query_handler(text=["technology", "economics", "medicine", "pedagogy"])
async def направления(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""

    if call.data == "technology":
        await call.message.answer("Technology")
        text = "Technology"
    elif call.data == "economics":
        await call.message.answer("Economics")
        text = "Economics"
    elif call.data == "medicine":
        await call.message.answer("Medicine")
        text = "Medicine"
    elif call.data == "pedagogy":
        await call.message.answer("Pedagogy")
        text = "Pedagogy"
    else:
        await call.message.answer("Please press one of the buttons!", reply_markup=keyboard2)
    
    cursor.execute("UPDATE users SET button_5 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()  
    
    

@dp.callback_query_handler(text=["sertifikat_1", "sertifikat_2", "sertifikat_3"])
async def sertifikat(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "sertifikat_1":
        await call.message.answer("Boshlangʻich sertifikat", reply_markup=keyboard11)
        text = "Boshlangʻich sertifikat"
    elif call.data == "sertifikat_2":
        await call.message.answer("Oʻrta sertifikat", reply_markup=keyboard11)
        text = "Oʻrta sertifikat"
    elif call.data == "sertifikat_3":
        await call.message.answer("Professional sertifikat", reply_markup=keyboard11)
        text = "Professional sertifikat"
    else:
        await call.message.answer("Iltimos, tugmalardan birini bosing!", reply_markup=keyboard2)
        
    cursor.execute("UPDATE users SET button_3 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    # await call.message.answer(f"Tanlagan sertifikat: {text}", reply_markup=keyboard11)
     
        
        
@dp.callback_query_handler(text=["сертификат_1", "сертификат_2", "сертификат_3"])
async def сертифика(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""

    if call.data == "сертификат_1":
        await call.message.answer("Начальный сертификат", reply_markup=keyboard12)
        text = "Начальный сертификат"
    elif call.data == "сертификат_2":
        await call.message.answer("Средний сертификат", reply_markup=keyboard12)
        text = "Средний сертификат"
    elif call.data == "сертификат_3":
        await call.message.answer("Профессиональный сертификат", reply_markup=keyboard12)
        text = "Профессиональный сертификат"
    else:
        await call.message.answer("Пожалуйста, нажмите одну из кнопок!", reply_markup=keyboard2)
        
    cursor.execute("UPDATE users SET button_3 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    # await call.message.answer(f"Tanlagan sertifikat: {text}", reply_markup=keyboard12)
    
       
        
@dp.callback_query_handler(text=["certificate_1", "certificate_2", "certificate_3"])
async def certificate(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "certificate_1":
        await call.message.answer("Initial certificate", reply_markup=keyboard13)
        text = "Initial certificate"
    elif call.data == "certificate_2":
        await call.message.answer("Average certificate", reply_markup=keyboard13)
        text = "Average certificate"
    elif call.data == "certificate_3":
        await call.message.answer("Professional certificate", reply_markup=keyboard13)
        text = "Professional certificate"
    else:
        await call.message.answer("Please press one of the buttons!", reply_markup=keyboard2)
    
    
    cursor.execute("UPDATE users SET button_3 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    # await call.message.answer(f"Tanlagan sertifikat: {text}", reply_markup=keyboard13)


@dp.callback_query_handler(text=["sertifikat_1", "sertifikat_2", "sertifikat_3"])
async def sertifikat(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "sertifikat_1":
        await call.message.answer("Boshlangʻich sertifikat", reply_markup=keyboard11)
        text = "Boshlangʻich sertifikat"
    elif call.data == "sertifikat_2":
        await call.message.answer("Oʻrta sertifikat", reply_markup=keyboard11)
        text = "Oʻrta sertifikat"
    elif call.data == "sertifikat_3":
        await call.message.answer("Professional sertifikat", reply_markup=keyboard11)
        text = "Professional sertifikat"
    else:
        await call.message.answer("Iltimos, tugmalardan birini bosing!", reply_markup=keyboard2)
        
    cursor.execute("UPDATE users SET button_3 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    # await call.message.answer(f"Tanlagan sertifikat: {text}", reply_markup=keyboard11)
    

@dp.callback_query_handler(text=["сертификат_1", "сертификат_2", "сертификат_3"])
async def сертифика(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""

    if call.data == "сертификат_1":
        await call.message.answer("Начальный сертификат", reply_markup=keyboard12)
        text = "Начальный сертификат"
    elif call.data == "сертификат_2":
        await call.message.answer("Средний сертификат", reply_markup=keyboard12)
        text = "Средний сертификат"
    elif call.data == "сертификат_3":
        await call.message.answer("Профессиональный сертификат", reply_markup=keyboard12)
        text = "Профессиональный сертификат"
    else:
        await call.message.answer("Пожалуйста, нажмите одну из кнопок!", reply_markup=keyboard2)
        
    cursor.execute("UPDATE users SET button_3 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    # await call.message.answer(f"Tanlagan sertifikat: {text}", reply_markup=keyboard12)
    
    
@dp.callback_query_handler(text=["certificate_1", "certificate_2", "certificate_3"])
async def certificate(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "certificate_1":
        await call.message.answer("Initial certificate", reply_markup=keyboard13)
        text = "Initial certificate"
    elif call.data == "certificate_2":
        await call.message.answer("Average certificate", reply_markup=keyboard13)
        text = "Average certificate"
    elif call.data == "certificate_3":
        await call.message.answer("Professional certificate", reply_markup=keyboard13)
        text = "Professional certificate"
    else:
        await call.message.answer("Please press one of the buttons!", reply_markup=keyboard2)
    
    
    cursor.execute("UPDATE users SET button_3 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close() 


executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    print("Starting bot...")
 