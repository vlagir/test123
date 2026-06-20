import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "8941070630:AAFplN0X1lzGVVI9IDYMZoTZHknpXwXhUuI"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message()
async def handler(message: types.Message):
    if message.text == "/start":
        await message.answer("🤖 Бот запущен и работает!")
    else:
        await message.answer(f"Ты написал: {message.text}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
