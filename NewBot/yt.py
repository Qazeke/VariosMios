#! /usr/bin/env python
# -*- coding:utf-8-*-
from __future__ import unicode_literals
import youtube_dl
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
ConversationHandler)

def download(bot, update, chat_id):
    ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s-%(id)s.%(ext)s',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
    }
    bot.sendMessage('Mete el link de youtube: ', chat_id)
    userlink = update.message.from_user;
    update.message.reply_text('Descargando y enviando...')

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([userlink])
    bot.send_audio(chat_id=chat_id, open=())   