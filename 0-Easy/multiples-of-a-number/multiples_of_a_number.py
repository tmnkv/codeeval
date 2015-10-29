import sys


for line in open(sys.argv[1]):
    x, n = int(line.split(",")[0]), int(line.split(",")[1])
    multiplier = 1
    while True:
        if x > n * multiplier:
            multiplier += 1
            continue
        else:
            print (n * multiplier)
            break