import sys


for line in open(sys.argv[1]):
    x, n = int(line.split(",")[0]), int(line.split(",")[1])
    i = 1
    while x > n * i:
        i += 1
    print(n * i)