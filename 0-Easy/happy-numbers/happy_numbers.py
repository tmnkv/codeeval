import sys


def is_it_happy(number):
    q = 1
    while True:
        summa = 0
        for i in number:
            summa += int(i) ** 2
        if summa == 1:
            return 1
        elif q == 10:
            return 0
        else:
            number = str(summa)
            q += 1

for line in open(sys.argv[1]):
    print(is_it_happy(line.rstrip()))

