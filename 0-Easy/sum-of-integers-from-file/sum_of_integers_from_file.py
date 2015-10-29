import sys

summa = 0
for line in open(sys.argv[1]):
    summa += int(line)
print(summa)