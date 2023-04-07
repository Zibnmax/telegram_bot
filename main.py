import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types


def config():
    
    load_dotenv()
    TOKEN = os.getenv("TOKEN")



