import asyncio
import logging
import sys
from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import dp, bot
from schedulers import start_scheduler

@dp.message(Command('start'))
async def start_command(message: Message):
    ikb = InlineKeyboardBuilder()
    ikb.row(
        InlineKeyboardButton(text="Avto Test", callback_data="avto_test"),
    )
    await message.answer(
        text="Assalomu alaykum xush kelibsiz!\nKerakli tugmani tanlang yoki link ustiga bosing ⬇️",
        reply_markup=ikb.as_markup()
    )

@dp.callback_query(F.data == 'avto_test')
async def avto_test(callback: CallbackQuery):
    await callback.message.answer("Siz So'ragan Avto_test!,\n\nhttp://t.me/pravaoluzbot/app")
    await callback.answer()
async def main():
    start_scheduler()
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())



