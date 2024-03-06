import asyncio



from decouple import config

from aiogram import Bot, Dispatcher, Router, types,F
from aiogram.utils import keyboard
from aiogram.filters import CommandStart, Command   
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


TOKEN = config("TOKEN")

dp = Dispatcher() 
bot = Bot(TOKEN)


start_kb = keyboard.InlineKeyboardBuilder()
start_kb.row(types.InlineKeyboardButton(text="Дізнатися більше", callback_data="more"))

statistic = {
    "answer_1" : 0,
    "answer_2" : 0,
    "answer_3" : 0
}

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    spray_link = ("https://th.bing.com/th/id/OIG1.vfbQag1vrcSPfb1HTurY?pid=ImgGn")
    await bot.send_photo(message.chat.id, spray_link)
    await message.answer("Привіт..Хочеш дізнатися більше про наш винахід?", reply_markup=start_kb.as_markup())

@dp.callback_query(F.data=="more")
async def more_info(call: types.CallbackQuery):
    
    start_kb1 = keyboard.InlineKeyboardBuilder()
    start_kb1.row(types.InlineKeyboardButton(text="Зворотній зв'язок📞👀", url="https://www.google.com"))
    start_kb1.row(types.InlineKeyboardButton(text="Дізнатися більше👍", callback_data="feedback"))
    await call.message.edit_text("Наш винахід - це найкращий в світі винахід!🆒", reply_markup=start_kb1.as_markup())

@dp.callback_query(F.data=="feedback")
async def feedback(call: types.CallbackQuery):
    markup = keyboard.InlineKeyboardBuilder()
    markup.add(types.InlineKeyboardButton(text="Вражаюче!❤", callback_data="answer_1"))
    markup.add(types.InlineKeyboardButton(text="Цікаво, але можна ще покращи-+", callback_data="answer_2"))
    markup.add(types.InlineKeyboardButton(text="Не вражає(((", callback_data="answer_3"))
    
    await call.message.edit_text("Що ви думаєте про наш новий гаджет?", reply_markup=markup.as_markup())
    
@dp.callback_query(F.data.startswith('answer_'))
async def answer(call: types.CallbackQuery):
    statistic[call.data] += 1
    await call.message.edit_text("Дякуємо за відгук!❤")


@dp.message(Command("statistic"))
async def get_statistic(message: types.Message):
    await message.answer(f"Вражає: {statistic['answer_1']}\n\
                        Цікаво, але можна ще покращити: {statistic['answer_2']}\n\
                        Не вражає: {statistic['answer_3']}")

@dp.message(Command("help"))
async def get_statistic(message: types.Message):
    spray_link = ("https://th.bing.com/th/id/OIG1.vfbQag1vrcSPfb1HTurY?pid=ImgGn")
    await bot.send_photo(message.chat.id, spray_link)
    kkkk = keyboard.ReplyKeyboardBuilder()
    kkkk.add(types.KeyboardButton(text="Так, хочу дізнатися більше"))
    kkkk.add(types.KeyboardButton(text="Ні, дякую"))
    await message.answer("Бажаєте отримати більше інформації про наш гаджет?", reply_markup=kkkk.as_markup())
    
@dp.message()
async def unknown(message: types.Message):
    if message.text == "Так, хочу дізнатися більше":
        answer = "Тоді перейдіть за посиланням: https://www.google.com"
    elif message.text == "Ні, дякую":
        answer = "Дякуємо за увагу!"
    else:
        answer = "Я не розумію вас. Доступні команди: /start, /help"
    await message.answer(answer, reply_markup=types.ReplyKeyboardRemove())
    
    await message.answer("Головне меню", reply_markup=start_kb.as_markup())

@dp.message(Command("help"))
async def maybe_help(message: types.Message):
    await message.answer("тут покачто нечё нет ")
# 
async def main() -> None:
    await dp.start_polling(bot)
# 
if __name__ == "__main__":
    asyncio.run(main())
