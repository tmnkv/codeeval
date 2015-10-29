import sys


for line in open(sys.argv[1]):
    n, p1, p2 = [int(line.split(",")[i]) for i in range(3)]
    if bin(n)[-p1] == bin(n)[-p2]:
        print("true")
    else:
        print("false")
