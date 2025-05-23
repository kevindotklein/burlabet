from burlabet.bot.decorators import require_admin
from telegram import Update
from telegram.ext import ContextTypes
import burlabet.db.db as db

@require_admin("Command: '/get_users'", "Permission denied: '/get_users'", "Usuário não autorizado")
async def get_users(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  users = [str(u) for u in db.get_users()]
  users_str = '\n'.join(users)
  await update.message.reply_text(f"{users_str}")

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
