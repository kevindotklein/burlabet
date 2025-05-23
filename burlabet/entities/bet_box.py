from typing import List
from burlabet.entities.booker import Booker

class BetBox:
  def __init__(self, profit: str, posted_at: str, bookers: List[Booker]) -> None:
    self.profit = profit
    self.posted_at = posted_at
    self.bookers: List[Booker] = bookers
  
  def __str__(self) -> str:
    bookers_str: List[str] = ["" + str(b) for b in self.bookers]
    return f"BetBox(profit = '{self.profit}' posted_at='{self.posted_at}' bookers=[\n" + "\n".join(bookers_str) + "\n])"
  
  def to_html(self) -> str:
    html = (
      f'💵 <b>Lucro</b>: {self.profit}\n'
      f'⌛ <b>Há</b>: {self.posted_at}\n'
    )
    bookers_str = [b.to_html() + '\n' for b in self.bookers]
    return html + '\n' + "".join(bookers_str)