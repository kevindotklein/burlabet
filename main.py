from burlabet.scrapper.user.user_feed import get_user_bets
from burlabet.db.db import init_db, add_user, get_users, get_user
from burlabet.bot.bot import bot_run

def main() -> None:
  init_db()
  boxes = get_user_bets(1)
  debug_str = [b.to_html() for b in boxes]
  for x in debug_str:
    print(x)
  bot_run()

if __name__ == '__main__':
  main()