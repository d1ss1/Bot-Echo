import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

TOKEN = "Token"

# Списки спец ответов
LOX = ["Ты лох!", "ты лох!"]
DURAK = ["Ты дурак", "ты дурак", "ТЫ ДУРАК"]

async def reply_echo(message: Message) -> None:
    """Умный эхо-бот с командами и защитой"""
    text = message.text or "(пусто)"
    
    # спец команды
    if text == "привет":
        await message.answer("Привет! Я EchoBot! 🤖")
    elif text == "пока":
        await message.answer("До встречи! 👋")
    elif text in LOX:
        await message.answer("Нет ты лох! 😤")
    elif text in DURAK:
        await message.answer("Нет ты дурак! 😤")
    else:
        # обычное эхо
        await message.answer(text)

async def main() -> None:
    """Запуск бота"""
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Очищаем webhook
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        print("✅ Webhook очищен")
    except Exception as e:
        print(f"⚠️ Ошибка: {e}")

    # Регистрируем обработчик
    dp.message.register(reply_echo)

    print("🤖 Smart Echo Bot запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
