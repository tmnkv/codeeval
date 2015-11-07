import sys


def compute_difference(houses, house):
    difference = 0
    for h in houses:
        difference += abs(h - house)
    return difference

for line in open(sys.argv[1]):
    houses = sorted([int(x) for x in line.rstrip().split()[1:]])
    difference = 500000
    for house in range(min(houses), max(houses) + 1):
        difference = min(difference, compute_difference(houses, house))
    print(difference)


