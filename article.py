import sqlite3


from telegram import *
from aiogram.types import CallbackQuery
from buttons import keyboard1, keyboard2, keyboard3, keyboard4, keyboard5, keyboard6, keyboard7, keyboard8, keyboard9, keyboard10, keyboard11, keyboard12, keyboard13
from bot import dp


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
        await call.message.answer("Yozib berish!", reply_markup=keyboard11)
        text = "Yozib berish!"
    elif call.data == "yozish_chop_etish":
        await call.message.answer("Yozib berish va chop etish!", reply_markup=keyboard11)
        text = "Yozib berish va chop etish!"
    elif call.data == "chop_etish":
        await call.message.answer("Tayyor maqolani chop etish!", reply_markup=keyboard11)
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
        await call.message.answer("Написать!", reply_markup=keyboard12)
        text = "Написать!"
    elif call.data == "написать_распечатать":
        await call.message.answer("Написать и распечатать!", reply_markup=keyboard12)
        text = "Написать и распечатать!"
    elif call.data == "распечатать":
        await call.message.answer("Распечатать готовую статью!", reply_markup=keyboard12)
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
        await call.message.answer("Write!", reply_markup=keyboard13)
        text = "Write!"
    elif call.data == "write_print":
        await call.message.answer("Write and print!", reply_markup=keyboard13)
        text = "Write and print!"
    elif call.data == "print":
        await call.message.answer("Print a finished article!", reply_markup=keyboard13)
        text = "Print a finished article!"
    else:
        await call.message.answer("Please press one of the buttons!", reply_markup=keyboard2)
    
    cursor.execute("UPDATE users SET button_4 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    

