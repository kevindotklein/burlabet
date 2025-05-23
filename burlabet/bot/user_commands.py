from burlabet.bot.decorators import require_user
from telegram import Update
from telegram.ext import ContextTypes
from burlabet.scrapper.user.user_feed import get_user_bets

@require_user("Command: '/bets'", "Invalid user: '/bets'", "A sua conta está inválida, para clique aqui: /help")
async def get_bets(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  boxes = get_user_bets(10)
  for b in boxes:
    await update.message.reply_text(f"{b.to_html()}", parse_mode="HTML")