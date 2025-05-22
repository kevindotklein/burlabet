import os
from typing import List, Final
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from burlabet.utils.print_c import print_c, Color
import burlabet.db.db as db

load_dotenv()

ADMINS: Final[List[int]] = [6931245709, 708384386]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  user_id = update.effective_user.id
  print(f"{user_id}")
  await update.message.reply_text("test /premium")

async def get_users(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  user_id = update.effective_user.id
  if user_id not in ADMINS:
    await update.message.reply_text("Usuário não autorizado")
    return
  users = [str(u) for u in db.get_users()]
  users_str = '\n'.join(users)
  await update.message.reply_text(f"{users_str}")

async def get_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  if not context.args:
    await update.message.reply_text("❗ Especifique um ID. Ex: /get_user 0")
    return
  user_id = update.effective_user.id
  if user_id not in ADMINS:
    await update.message.reply_text("Usuário não autorizado")
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

  print_c("Telegram BurlaBet Bot running...", Color.GREEN)
  app.run_polling()