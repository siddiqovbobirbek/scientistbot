import logging
import sqlite3
import telebot

from telegram import *
from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from buttons import keyboard1, keyboard2, keyboard3, keyboard4, keyboard5, keyboard6, keyboard7, keyboard8, keyboard9, keyboard10, keyboard11, keyboard12, keyboard13
from bot import dp, bot




executor.start_polling(dp, skip_updates=True)



if __name__ == '__main__':
    print("Starting bot...")
