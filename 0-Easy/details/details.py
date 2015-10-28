import sys


for line in open(sys.argv[1]):
    rows = line.split(",")
    moves = [row.count(".", len(row) - row[::-1].find("X") - 1, row.find("Y")) for row in rows]
    moves.sort()
    print(moves[0])
