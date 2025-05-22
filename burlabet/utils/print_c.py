from enum import Enum
from typing import Final

class Color(Enum):
  BLACK   = "\033[30m"
  RED     = "\033[31m"
  GREEN   = "\033[32m"
  YELLOW  = "\033[33m"
  BLUE    = "\033[34m"
  MAGENTA = "\033[35m"
  CYAN    = "\033[36m"
  WHITE   = "\033[37m"
  RESET   = "\033[0m"

def print_c(text: str, color: Color) -> None:
  print(f"{color.value}{text}{Color.RESET.value}")