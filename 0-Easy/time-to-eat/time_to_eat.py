import sys


for line in open(sys.argv[1]):
    schedule = line.split()
    schedule.sort(reverse=True)
    print(" ".join(schedule))