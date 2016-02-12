import sys


for line in open(sys.argv[1]):
    lists = line.rstrip().split(";")
    l1, l2 = [set(l.split(",")) for l in lists]
    intersection = list(l1.intersection(l2))
    print(",".join(sorted(intersection)))
