import sys


for line in open(sys.argv[1]):
    rows = line.split("|")
    table = [rows[i].split() for i in range(len(rows))]
    for i in range(len(rows)):
        table[i] = [int(x) for x in table[i]]
    for j in range(len(table[0])):
        print(max([table[i][j] for i in range(len(table))]), end=" ")
    print()
