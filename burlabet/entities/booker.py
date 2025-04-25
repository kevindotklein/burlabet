
class Booker:

  def __init__(self, name: str, link: str, date_time: str, coeff: str, odd_value: str, odd_link: str) -> None:
    self.name = name
    self.link = link
    self.date_time = date_time
    self.coeff = coeff
    self.odd_value = odd_value
    self.odd_link = odd_link
  
  def __str__(self):
    return f"Booker(name='{self.name}' link='{self.link}' date_time='{self.date_time}' " \
      f"coeff='{self.coeff}' odd_value='{self.odd_value}' odd_link='{self.odd_link}')"