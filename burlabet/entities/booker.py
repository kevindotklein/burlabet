
class Booker:

  def __init__(self, name: str, link: str, date_time: str, coeff: str, odd_value: str, odd_link: str) -> None:
    self.name = name
    self.link = link
    self.date_time = date_time
    self.coeff = coeff
    self.odd_value = odd_value
    self.odd_link = odd_link
  
  def __str__(self):
    return f"Booker(\n\tname='{self.name}' \n\tlink='{self.link}' \n\tdate_time='{self.date_time}' " \
      f"\n\tcoeff='{self.coeff}' \n\todd_value='{self.odd_value}' \n\todd_link='{self.odd_link}'\n)"