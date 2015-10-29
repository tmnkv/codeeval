import sys


for line in open(sys.argv[1]):
    lists = line.rstrip().split(";")
    l1, l2 = [l.split(",") for l in lists]
    inrersection = list(set(l1).intersection(set(l2)))
    inrersection.sort()
    print(",".join(inrersection))