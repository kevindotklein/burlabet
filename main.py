from burlabet.scrapper.user.user_feed import get_user_bets
from burlabet.db.db import init_db, add_user, get_users, get_user

def main() -> None:
  init_db()
  # boxes = get_user_bets(3)
  # debug_str = [str(b) for b in boxes]
  # for x in debug_str:
  #   print(x)

  users = get_users()
  users_str = [str(u) for u in users]
  for x in users_str:
    print(x)
  print("="*60)
  user1 = get_user(1)
  if not user1:
    print("usuário 1 n encontrado")
  print(user1)

if __name__ == '__main__':
  main()