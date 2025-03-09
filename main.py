import asyncio
import os
from loguru import logger
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")


async def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True,
               diagnose=True)
    
    bot = Bot(TOKEN)
    logger.info("Бот создан")
    dp = Dispatcher()
    logger.info("Диспетчер создан")
    
    @dp.message(Command("start"))
    async def send_welcome(message: types.Message):
        await message.answer("привет, Я гей бот!")
        logger.info("бот отетил на команду /start")
        
    @dp.message(Command("help"))
    async def help(message: types.Message):
        await message.answer("у тебя проблема? сейчас уладим!)")
        logger.info("бот обьяснил что делвет")
        
    @dp.message()
    async def echo(message):
        await message.answer(message.txt)
        logger.info(f"Бот вернул пользователю сообщение{message.text}")

    await dp.start_polling(bot)
  
if __name__ == '__main__':
    asyncio.run(main())
