from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F
from random import randint

API = "#"

bot = Bot(API)
disp = Dispatcher()

async def process_start_command(message: Message):
    global random_num
    global attempts
    
    random_num = randint(1, 100)
    attempts = 5
    
    await message.answer('Привет! Сыграем в игру: я загадаю число от 1 до 100, ' 
                         'а тебе нужно отгадать его за 5 попыток.')
    await message.answer("Я готов. Начинай!")
    
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне /start'
    )

async def send_game_message(message: Message):
    global attempts
    
    attempts -= 1
    
    try:
        user_text = int(message.text)
        
        if user_text < random_num and attempts != 0: await message.answer(f"Моё число больше! Осталось {attempts} попыток.")
        elif user_text > random_num and attempts != 0: await message.answer(f"Моё число меньше. Осталось {attempts} попыток.")
        elif user_text == random_num and attempts != 0: await message.answer(f"Ты отгадал(а) число - {random_num}. Всего {attempts+1} попыток. Напиши /start, чтобы сыграть ещё раз")
        elif attempts == 0: 
            await message.answer("Использованы все попытки! К сожалению, ты проиграл(а). Напиши /start, чтобы сыграть ещё раз")
            return
        
    except: await message.answer("Введи число!")

disp.message.register(process_start_command, Command(commands='start'))
disp.message.register(process_help_command, Command(commands='help'))
disp.message.register(send_game_message)

if __name__ == '__main__': disp.run_polling(bot)