from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

API = "#"

bot = Bot(API)
disp = Dispatcher()

@disp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')
    
@disp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )
    
@disp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)
    
if __name__ == '__main__': disp.run_polling(bot)