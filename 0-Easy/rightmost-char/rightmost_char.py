import sys


for line in open(sys.argv[1]):
    S, t = line.rstrip().split(",")
    print("{0}".format(S.rfind(t)))
