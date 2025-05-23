import os
from typing import List, Final
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import burlabet.db.db as db
import burlabet.utils.log as log
from burlabet.scrapper.user.user_feed import get_user_bets
from burlabet.bot.decorators import require_admin, guest, require_user
from burlabet.bot.constants import START_MSG

load_dotenv()

@guest("Command: '/start'")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  # user_id = update.effective_user.id
  # log.info(user_id, "Command: '/start'")
  await update.message.reply_text(START_MSG, parse_mode="HTML")

@require_admin("Command: '/get_users'", "Permission denied: '/get_users'", "Usuário não autorizado")
async def get_users(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  users = [str(u) for u in db.get_users()]
  users_str = '\n'.join(users)
  await update.message.reply_text(f"{users_str}")

@require_user("Command: '/bets'", "Invalid user: '/bets'", "A sua conta está inválida, para clique aqui: /help")
async def get_bets(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  boxes = get_user_bets(10)
  for b in boxes:
    await update.message.reply_text(f"{b.to_html()}", parse_mode="HTML")

@require_admin(f"Command: '/get_user <ID>'", "Permission denied: '/get_user <ID>'", "Usuário não autorizado")
async def get_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  if not context.args:
    await update.message.reply_text("❗ Especifique um ID. Ex: /get_user 0")
    return
  req_id = context.args[0]
  try:
    int(req_id)
  except ValueError:
    await update.message.reply_text("❗O ID deve ser um número")
    return
  user = db.get_user(int(req_id))
  if not user:
    await update.message.reply_text(f"❗Usuário com ID: {req_id} não encontrado")
    return

  await update.message.reply_text(f"{str(user)}")


def bot_run() -> None:
  app = ApplicationBuilder().token(token=os.getenv("BOT_TOKEN")).build()

  app.add_handler(CommandHandler("start", start))
  app.add_handler(CommandHandler("get_users", get_users))
  app.add_handler(CommandHandler("get_user", get_user))
  app.add_handler(CommandHandler("bets", get_bets))

  log.bot("Telegram BurlaBet Bot running...")
  app.run_polling()