from typing import Dict, Final
from requests import Response
import requests
from bs4 import BeautifulSoup
import datetime
import sys
from burlabet.utils.io_utils import terminal_hyperlink

def main() -> None:
  URL: Final[str] = "https://pt.surebet.com/surebets"
  TABLE_WIDTH: Final[int] = 90

  headers: Dict[str, str] = {
    "User-Agent": "Mozilla/5.0"
  }

  res: Response = requests.get(URL, headers=headers)
  soup: BeautifulSoup = BeautifulSoup(res.text, "html.parser")

  bets = soup.find_all("tbody", class_="surebet_record")

  for b in bets:
    print("=" * TABLE_WIDTH)
    # profit
    profit_box = b.select_one("tr>td.profit-box")
    profit = profit_box.find("span", class_ = "profit ps-2 cursor-help")

    # posted at
    posted_at = profit_box.find("span", class_ = "age ps-2 cursor-help")

    if profit and posted_at:
      print(f"| Lucro: {profit.text.strip()}".ljust(TABLE_WIDTH//2), f"Postado há: {posted_at.text.strip()} |".rjust((TABLE_WIDTH//2)-1))
      print("-" * TABLE_WIDTH)

    trs = b.find_all("tr")
    for tr in trs:
      # booker
      booker_box = tr.find("td", class_ = "booker")
      if not booker_box:
        break
      booker = booker_box.find("a")

      # date time
      time_box = tr.find("td", class_ = "time")
      time = time_box.find("abbr")
      utc = time.get("data-utc")
      date_time = datetime.datetime.fromtimestamp(int(utc)/1000)
      formatted_date = date_time.strftime("%d/%m %H:%M")

      # coeff
      coeff_box = tr.find("td", class_ = "coeff")
      coeff = coeff_box.find("abbr")

      # odd
      odd_box = tr.find("td", class_ = "value")
      odd_link = odd_box.select_one("div>a.value_link")
      hyperlink: str = "odd: " + terminal_hyperlink(URL[:22] + odd_link.get('href'), odd_link.text.strip()) + " |\n"


      sys.stdout.write(f"| {booker.text.strip()}".ljust(25) + f"{formatted_date} " + f"{coeff.text.strip()}".center(30)
                       + hyperlink.rjust(145))
      sys.stdout.flush()

    print("=" * TABLE_WIDTH, "\n")

if __name__ == '__main__':
  main()