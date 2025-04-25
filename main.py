from burlabet.scrapper.guest.guest_feed import get_guest_bets

def main() -> None:
  boxes = get_guest_bets(3)
  debug_str = [str(b) for b in boxes]
  for x in debug_str:
    print(x)

if __name__ == '__main__':
  main()