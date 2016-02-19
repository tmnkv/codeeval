import sys

RANKS = dict(zip(['2','3','4','5','6','7','8','9','10','J','Q','K','A'],
                 range(2, 15)))


def who_is_bigger(cards):
    if RANKS[cards[0][:-1]] > RANKS[cards[1][:-1]]:
        return cards[0]
    elif RANKS[cards[0][:-1]] < RANKS[cards[1][:-1]]:
        return cards[1]
    else:
        return ' '.join(cards)



def main(input_file):
  fh = open(input_file)
  for line in fh:
    cards, trump = line.rstrip().split(' | ')
    cards = cards.split()
    istrump = [x.count(trump) for x in cards]
    if istrump[0] == istrump[1]:
        result = who_is_bigger(cards)
    else:
        result = cards[istrump.index(1)]
    print(result)


main(sys.argv[1])
