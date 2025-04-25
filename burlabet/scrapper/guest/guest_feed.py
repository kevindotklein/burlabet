from burlabet.entities.bet_box import BetBox
from burlabet.entities.booker import Booker
from burlabet.scrapper.constants import URL, URL_HOME, GUEST_HEADERS
from typing import List
from bs4 import BeautifulSoup
import requests
import datetime
import itertools

def get_guest_bets(range: int = 25) -> List[BetBox]:
  res = requests.get(URL + URL_HOME, headers=GUEST_HEADERS)
  soup = BeautifulSoup(res.text, "html.parser")

  bets = soup.find_all("tbody", class_="surebet_record")

  boxes: List[BetBox] = []

  for b in itertools.islice(bets, range):
    # profit
    profit_box = b.select_one("tr>td.profit-box")
    profit = profit_box.find("span", class_ = "profit ps-2 cursor-help")

    # posted at
    posted_at = profit_box.find("span", class_ = "age ps-2 cursor-help")

    bet = BetBox(profit.text.strip(), posted_at.text.strip(), [])

    trs = b.find_all("tr")
    for tr in trs:
      # booker
      booker_box = tr.find("td", class_ = "booker")
      if not booker_box:
        break
      booker_elem = booker_box.find("a")

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

      booker = Booker(booker_elem.text.strip(), booker_elem.get('href'), formatted_date,
                      coeff.text.strip(), odd_link.text.strip(), odd_link.get('href'))
      bet.bookers.append(booker)
    
    boxes.append(bet)
  return boxes