class User:

  def __init__(self, id: int, expires_at: str) -> None:
    self.id = id
    self.expires_at = expires_at

  def __str__(self):
    return f"👤 (\n\tid='{self.id}' \n\texpires_at='{self.expires_at}'\n)"