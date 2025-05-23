import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler
import burlabet.utils.log as log
import burlabet.bot.admin_commands as admin_commands
import burlabet.bot.guest_commands as guest_commands
import burlabet.bot.user_commands as user_commands

load_dotenv()

def bot_run() -> None:
  app = ApplicationBuilder().token(token=os.getenv("BOT_TOKEN")).build()

  app.add_handler(CommandHandler("start", guest_commands.start))
  app.add_handler(CommandHandler("get_users", admin_commands.get_users))
  app.add_handler(CommandHandler("get_user", admin_commands.get_user))
  app.add_handler(CommandHandler("bets", user_commands.get_bets))
  app.add_handler(CommandHandler("get_telegram_id", guest_commands.get_telegram_id))
  app.add_handler(CommandHandler("add_user", admin_commands.add_user))

  log.bot("Telegram BurlaBet Bot running...")
  app.run_polling()