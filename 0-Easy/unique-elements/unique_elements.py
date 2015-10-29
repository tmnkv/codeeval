import sys


for line in open(sys.argv[1], "r"):
    test = sorted(set([int(i) for i in line.rstrip().split(",")]))
    print(",".join((str(i) for i in test)))
