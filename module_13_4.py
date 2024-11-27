 Домашнее задание по теме "Хендлеры обработки сообщений".

# импорт необходимых библиотек и методов
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

# api ключ, который мы получили в «BotFather». Переменная бота,
# хранящая объект бота, «token» будет равен вписанному ключу
api = "7521487732:AAFPNCs4QV7XC5p0HDUbhZEjNg49-TAYYiM"  # введите Ваш api полученный в @BotFather
bot = Bot(token=api)
# переменная dp объекта «Dispatcher», у него наш бот в
# качестве аргументов. В качестве «Storage» будет «MemoryStorage»
dp = Dispatcher(bot, storage=MemoryStorage())


# декоратор команды "start"
@dp.message_handler(commands=['start'])
async def start(message):
    # для ответа на команду обращаемся к ожидающему методу функции message.answer
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    # print('Привет! Я бот помогающий твоему здоровью.')


# декоратор, реагирующий на любые сообщения
@dp.message_handler()
async def all_message(message):
    # для ответа на сообщение обращаемся к ожидающему методу функции message.answer
    await message.answer('Введите команду /start, чтобы начать общение.')
    # print('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    # запуск бота (dp - аргумент через что стартовать)
    executor.start_polling(dp, skip_updates=True)