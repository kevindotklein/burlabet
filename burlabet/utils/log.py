from burlabet.utils.print_c import print_c, Color
import datetime

def bot(msg: str) -> None:
  print_c(f"[BOT] {msg} | At: {datetime.datetime.now()}", Color.GREEN)

def info(user_id: int, msg: str) -> None:
  print_c(f"[INFO] User: {user_id} | {msg} | At: {datetime.datetime.now()}", Color.CYAN)

def warn(user_id: int, msg: str) -> None:
  print_c(f"[WARN] User: {user_id} | {msg} | At: {datetime.datetime.now()}", Color.YELLOW)