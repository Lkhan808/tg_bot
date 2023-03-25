import datetime

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import ADMIN, bot
from apscheduler.triggers.cron import CronTrigger


async def homework1(bot: Bot):
    user_id = ADMIN[0]
    await bot.send_message(user_id, "Сделай домашку а то дедлайн пропустишь!!!")


async def homework2(bot: Bot):
    user_id = ADMIN[0]
    await bot.send_message(user_id, "Сделай домашку в то дедлайн пропустишь!!!")


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")
    scheduler.add_job(homework1, trigger=CronTrigger(day_of_week=2, hour=12, minute=00), kwargs={"bot": bot})
    scheduler.start()
    # scheduler.timezone=
