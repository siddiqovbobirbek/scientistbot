import logging
import sqlite3
import telebot

from telegram import *
from aiogram import Bot, Dispatcher, executor
from aiogram.types import CallbackQuery
from buttons import keyboard1, keyboard2, keyboard3, keyboard4, keyboard5, keyboard6, keyboard7, keyboard8, keyboard9, keyboard10, keyboard11, keyboard12, keyboard13
from bot import dp, bot



@dp.callback_query_handler(text=["sertifikat_1", "sertifikat_2", "sertifikat_3"])
async def sertifikat(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "sertifikat_1":
        text = "Boshlangʻich sertifikat"
    elif call.data == "sertifikat_2":
        text = "Oʻrta sertifikat"
    elif call.data == "sertifikat_3":
        text = "Professional sertifikat"
    
    cursor.execute("UPDATE users SET button_3 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    await call.message.answer(f"Tanlagan sertifikat: {text}", reply_markup=keyboard11)
    
    # if call.data == "sertifikat_1":
    #     await call.message.answer("Boshlangʻich sertifikat", reply_markup=keyboard11)
    # elif call.data == "sertifikat_2":
    #     await call.message.answer("Oʻrta sertifikat", reply_markup=keyboard11)
    # elif call.data == "sertifikat_3":
    #     await call.message.answer("Professional sertifikat", reply_markup=keyboard11)
    # else:
    #     await call.message.answer("Iltimos, tugmalardan birini bosing!", reply_markup=keyboard2)
        
        
        
@dp.callback_query_handler(text=["сертификат_1", "сертификат_2", "сертификат_3"])
async def сертифика(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "сертификат_1":
        text = "Начальный сертификат"
    elif call.data == "сертификат_2":
        text = "Средний сертификат"
    elif call.data == "сертификат_3":
        text = "Профессиональный сертификат"
    
    cursor.execute("UPDATE users SET button_3 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    await call.message.answer(f"Tanlagan sertifikat: {text}", reply_markup=keyboard12)
    
    # if call.data == "сертификат_1":
    #     await call.message.answer("Начальный сертификат", reply_markup=keyboard12)
    # elif call.data == "сертификат_2":
    #     await call.message.answer("Средний сертификат", reply_markup=keyboard12)
    # elif call.data == "сертификат_3":
    #     await call.message.answer("Профессиональный сертификат", reply_markup=keyboard12)
    # else:
    #     await call.message.answer("Пожалуйста, нажмите одну из кнопок!", reply_markup=keyboard2)
        
        
        
@dp.callback_query_handler(text=["certificate_1", "certificate_2", "certificate_3"])
async def certificate(call: CallbackQuery):
    connect = sqlite3.connect("sql.db")
    cursor = connect.cursor()
    user_id = call.from_user.id
    text = ""
    
    if call.data == "certificate_1":
        text = "Initial certificate"
    elif call.data == "certificate_2":
        text = "Average certificate"
    elif call.data == "certificate_3":
        text = "Professional certificate"
    
    cursor.execute("UPDATE users SET button_3 = ? WHERE id = ?", (text, int(user_id)))
    connect.commit()
    connect.close()
    
    await call.message.answer(f"Tanlagan sertifikat: {text}", reply_markup=keyboard13)
    # if call.data == "certificate_1":
    #     await call.message.answer("Initial certificate", reply_markup=keyboard13)
    # elif call.data == "certificate_2":
    #     await call.message.answer("Average certificate", reply_markup=keyboard13)
    # elif call.data == "certificate_3":
    #     await call.message.answer("Professional certificate", reply_markup=keyboard13)
    # else:
    #     await call.message.answer("Please press one of the buttons!", reply_markup=keyboard2)

executor.start_polling(dp, skip_updates=True)



if __name__ == '__main__':
    print("Starting bot...")
