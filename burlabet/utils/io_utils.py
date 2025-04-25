def terminal_hyperlink(url: str, text: str) -> str:
  return f'\x1b]8;;{url}\x1b\\{text}\x1b]8;;\x1b\\'