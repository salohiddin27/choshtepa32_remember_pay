import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv
from loader import bot

load_dotenv()
guruh_id = os.getenv("GURUH_ID")

scheduler = AsyncIOScheduler(timezone="Asia/Tashkent") # O'zbekiston vaqti bilan ishlashi uchun

async def send_daily_message():
    try:
        matn = (
            "Assalomu alaykum qardoshlar 👋\n"
            "iltimos kommunal to'lovni tekshirib qo'yaylik 📲\n\n"
            "agar to'lov qilsangiz guruhga check tashlashni unutmang😇\n\n"
            "1.Light code: 0293805\n2.Water code: 2628336808\n3.Gas code: 09271757\n4.Jeck code: 1393696170\n\n"
            "@akma1_577\n@PA70101\n@Javoh1r65_05\n@Mr_muhammadnur\n"
        )
        await bot.send_message(chat_id=guruh_id, text=matn)
    except Exception as e:
        print(f"Xabar yuborishda xatolik: {e}")

# Har kuni ertalab soat 08:00 da ishga tushadi (hour=8, minute=0)
scheduler.add_job(send_daily_message, "interval", seconds=2)

def start_scheduler():
    scheduler.start()