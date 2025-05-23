from burlabet.bot.constants import ADMINS
from functools import wraps
from telegram import Update
from telegram.ext import ContextTypes
import burlabet.utils.log as log
import burlabet.db.db as db

def is_user_admin(user_id: int) -> bool:
  return user_id in ADMINS

def require_admin(log_success: str, log_fail: str, msg_fail: str):
  def decorator(func):
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
      user_id = update.effective_user.id
      if not is_user_admin(user_id):
        log.warn(user_id, log_fail)
        await update.message.reply_text(f"{msg_fail}")
        return
      log.info(user_id, f"{log_success}")
      return await func(update, context, *args, **kwargs)
    return wrapper
  return decorator

def require_user(log_success: str, log_fail: str, msg_fail: str):
  def decorator(func):
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
      user_id = update.effective_user.id
      if not db.is_user_valid(user_id):
        log.warn(user_id, log_fail)
        await update.message.reply_text(f"{msg_fail}")
        return
      log.info(user_id, f"{log_success}")
      return await func(update, context, *args, **kwargs)
    return wrapper
  return decorator

def guest(log_success: str):
  def decorator(func):
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
      user_id = update.effective_user.id
      log.info(user_id, f"{log_success}")
      return await func(update, context, *args, **kwargs)
    return wrapper
  return decorator