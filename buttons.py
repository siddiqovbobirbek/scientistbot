import logging
import os

from telegram import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

button1 = KeyboardButton('🇺🇿 O\'zbekcha')
button2 = KeyboardButton('🇷🇺 Русский')
button3 = KeyboardButton('🇬🇧 English')
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2).add(button3)


button4 = InlineKeyboardButton(text = "Maqola", callback_data="maqola")
button5 = InlineKeyboardButton(text = "DGU", callback_data="dgu")
button6 = InlineKeyboardButton(text = "Sertifikat", callback_data="sertifikat")
keyboard2 = InlineKeyboardMarkup().add(button4).add(button5).add(button6)

button7 = InlineKeyboardButton(text = "Статья", callback_data="Статья")
button8 = InlineKeyboardButton(text = "ДГУ", callback_data="ДГУ")
button9 = InlineKeyboardButton(text = "Сертификат", callback_data="Сертификат")
keyboard3 = InlineKeyboardMarkup().add(button7).add(button8).add(button9)

button10 = InlineKeyboardButton(text = "Article", callback_data="article")
button11 = InlineKeyboardButton(text = "DGU", callback_data="patent")
button12 = InlineKeyboardButton(text = "Certificate", callback_data="certificate")
keyboard4 = InlineKeyboardMarkup().add(button10).add(button11).add(button12)

button13 = InlineKeyboardButton(text = "OAK uchun", callback_data="maqola_1")
button14 = InlineKeyboardButton(text = "Respublika konferensiya uchun", callback_data="maqola_2")
button15 = InlineKeyboardButton(text = "Xalqaro ilmiy jurnal uchun", callback_data="maqola_3")
button16 = InlineKeyboardButton(text = "Xalqaro konferensiya uchun", callback_data="maqola_4")
keyboard5 = InlineKeyboardMarkup().add(button13).add(button14).add(button15).add(button16)

button17 = InlineKeyboardButton(text = "Для OAC", callback_data="cтатья_1")
button18 = InlineKeyboardButton(text = "Для республиканской конференции", callback_data="cтатья_2")
button19 = InlineKeyboardButton(text = "Для международного научного журнала", callback_data="cтатья_3")
button20 = InlineKeyboardButton(text = "Для международной конференции", callback_data="cтатья_4")
keyboard6 = InlineKeyboardMarkup().add(button17).add(button18).add(button19).add(button20)

button21 = InlineKeyboardButton(text = "For OAC", callback_data="article_1")
button22 = InlineKeyboardButton(text = "For the Republican Conference", callback_data="article_2")
button23 = InlineKeyboardButton(text = "For an international scientific journal", callback_data="article_3")
button24 = InlineKeyboardButton(text = "For an international conference", callback_data="article_4")
keyboard7 = InlineKeyboardMarkup().add(button21).add(button22).add(button23).add(button24)

button_25 = InlineKeyboardButton(text = "Yozib berish!", callback_data="yozish")
button25 = InlineKeyboardButton(text = "Yozib berish va chop etish!", callback_data="yozish_chop_etish")
button26 = InlineKeyboardButton(text = "Tayyor maqolani chop etish!", callback_data="chop_etish")
keyboard8 = InlineKeyboardMarkup().add(button25).add(button26).add(button_25)


button_27 = InlineKeyboardButton(text = "Написать!", callback_data="написать")
button27 = InlineKeyboardButton(text = "Написать и распечатать!", callback_data="написать_распечатать")
button28 = InlineKeyboardButton(text = "Распечатать готовую статью!", callback_data="распечатать")
keyboard9 = InlineKeyboardMarkup().add(button27).add(button28).add(button_27)

button_29 = InlineKeyboardButton(text = "Write!", callback_data="write")
button29 = InlineKeyboardButton(text = "Write and print!", callback_data="write_print")
button30 = InlineKeyboardButton(text = "Print a finished article!", callback_data="print")
keyboard10 = InlineKeyboardMarkup().add(button29).add(button30).add(button_29)


button31 = InlineKeyboardButton(text = "Boshlangʻich sertifikat", callback_data="sertifikat_1")
button32 = InlineKeyboardButton(text = "Oʻrta sertifikat", callback_data="sertifikat_2")
button33 = InlineKeyboardButton(text = "Professional sertifikat", callback_data="sertifikat_3")
keyboard11 = InlineKeyboardMarkup().add(button31).add(button32).add(button33)

button34 = InlineKeyboardButton(text = "Начальный сертификат", callback_data="сертификат_1")
button35 = InlineKeyboardButton(text = "Средний сертификат", callback_data="сертификат_2")
button36 = InlineKeyboardButton(text = "Профессиональный сертификат", callback_data="сертификат_2")
keyboard12 = InlineKeyboardMarkup().add(button34).add(button35).add(button36)


button37 = InlineKeyboardButton(text = "Initial certificate", callback_data="certificate_1")
button38 = InlineKeyboardButton(text = "Intermediate certificate", callback_data="certificate_2")
button39 = InlineKeyboardButton(text = "Professional certificate", callback_data="certificate_2")
keyboard13 = InlineKeyboardMarkup().add(button37).add(button38).add(button39) 


