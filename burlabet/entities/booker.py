from burlabet.scrapper.constants import URL

class Booker:

  def __init__(self, name: str, link: str, date_time: str, coeff: str, odd_value: str, odd_link: str) -> None:
    self.name = name
    self.link = link
    self.date_time = date_time
    self.coeff = coeff
    self.odd_value = odd_value
    self.odd_link = odd_link
  
  def __str__(self) -> str:
    return f"Booker(\n\tname='{self.name}' \n\tlink='{self.link}' \n\tdate_time='{self.date_time}' " \
      f"\n\tcoeff='{self.coeff}' \n\todd_value='{self.odd_value}' \n\todd_link='{self.odd_link}'\n)"

  def to_html(self) -> str:
    html = (
      f'🏠 <a href="{URL + self.link}">{self.name}</a>\n'
      f'⌚ <b>{self.date_time}</b>\n'
      f'🎈 <b>{self.coeff}</b>\n'
      f'💸 <b>Odd</b>: <a href="{URL + self.odd_link}">{self.odd_value}</a>\n'
    )
    return html