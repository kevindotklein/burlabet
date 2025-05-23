from burlabet.bot.decorators import guest
from telegram import Update
from telegram.ext import ContextTypes
from burlabet.bot.constants import START_MSG

@guest("Command: '/start'")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  await update.message.reply_text(START_MSG, parse_mode="HTML")