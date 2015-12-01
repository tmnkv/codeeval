import sys


def black_card(line):
    line1, line2 = line.rstrip().split(" | ")
    players = line1.split()
    number = int(line2)
    for i in range(len(players) - 1):
        players.pop(number % len(players) - 1)
    return players[0]


def main(input_file):
    fh = open(input_file, "r")
    for line in fh:
        res = black_card(line)
        print(res)
    fh.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage {0} <input_file>".format(sys.argv[0]))
        sys.exit(1)
    main(sys.argv[1])
