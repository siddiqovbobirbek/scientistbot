import sqlite3


from telegram import *
from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.types import CallbackQuery
from buttons import keyboard1, keyboard2, keyboard3, keyboard4, keyboard5, keyboard6, keyboard7, keyboard8, keyboard9, keyboard10, keyboard11, keyboard12, keyboard13
from bot import dp, bot


@dp.callback_query_handler(text=["maqola_1", "maqola_2", "maqola_3", "maqola_4"])
async def maqola_yozish(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""

    if call.data == "maqola_1":
        text = "OAK uchun"
    elif call.data == "maqola_2":
        text = "Respublika konferensiya uchun"
    elif call.data == "maqola_3":
        text = "Xalqaro ilmiy jurnal uchun"
    elif call.data == "maqola_4":
        text = "Xalqaro konferensiya uchun"
    
    cursor.execute("UPDATE users SET button_2 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    if call.data == "maqola_1":
        await call.message.answer("OAK uchun", reply_markup=keyboard8)
    elif call.data == "maqola_2":
        await call.message.answer("Respublika konferensiya uchun", reply_markup=keyboard8)
    elif call.data == "maqola_3":
        await call.message.answer("Xalqaro ilmiy jurnal uchun", reply_markup=keyboard8)
    elif call.data == "maqola_4":
        await call.message.answer("Xalqaro konferensiya uchun", reply_markup=keyboard8)
    else:
        await call.message.answer("Iltimos, tugmalardan birini bosing!", reply_markup=keyboard2)

    
    # await call.message.answer(f"Tanlagan maqola: {text}", reply_markup=keyboard8)


@dp.callback_query_handler(text=["cтатья_1", "cтатья_2", "cтатья_3", "cтатья_4"])
async def maqola_yozish(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "cтатья_1":
        text = "Для OAC"
    elif call.data == "cтатья_2":
        text = "Для республиканской конференции"
    elif call.data == "cтатья_3":
        text = "Для международного научного журнала"
    elif call.data == "cтатья_4":
        text = "Для международной конференции"
    
    
    cursor.execute("UPDATE users SET button_2 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    await call.message.answer(f"Tanlagan maqola: {text}", reply_markup=keyboard9)
    
    if call.data == "cтатья_1":
        await call.message.answer("Для OAC", reply_markup=keyboard9)
    elif call.data == "cтатья_2":
        await call.message.answer("Для республиканской конференции", reply_markup=keyboard9)
    elif call.data == "cтатья_3":
        await call.message.answer("Для международного научного журнала", reply_markup=keyboard9)
    elif call.data == "cтатья_4":
        await call.message.answer("Для международной конференции", reply_markup=keyboard9)
    else:
        await call.message.answer("Пожалуйста, нажмите одну из кнопок!", reply_markup=keyboard2)
        
        
        
        
@dp.callback_query_handler(text=["article_1", "article_2", "article_3", "article_4"])
async def maqola_yozish(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "article_1":
        text = "For OAC"
    elif call.data == "article_2":
        text = "For the Republican Conference"
    elif call.data == "article_3":
        text = "For an international scientific journal"
    elif call.data == "article_4":
        text = "For an international conference"
    
    cursor.execute("UPDATE users SET button_2 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    await call.message.answer(f"Tanlagan maqola: {text}", reply_markup=keyboard10)
    
    if call.data == "article_1":
        await call.message.answer("For OAC", reply_markup=keyboard10)
    elif call.data == "article_2":
        await call.message.answer("For the Republican Conference", reply_markup=keyboard10)
    elif call.data == "article_3":
        await call.message.answer("For an international scientific journal", reply_markup=keyboard10)
    elif call.data == "article_4":
        await call.message.answer("For an international conference", reply_markup=keyboard10)
    else:
        await call.message.answer("Please press one of the buttons!", reply_markup=keyboard2)
        
        
executor.start_polling(dp, skip_updates=True)




if __name__ == '__main__':
    print("Starting bot...")

