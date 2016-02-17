import sys
from datetime import datetime


def main(input_file):
    fh = open(input_file)
    for line in fh:
        time1, time2 = [datetime.strptime(x, '%H:%M:%S') for x in line.rstrip().split()]
        delta = time1 - time2 if time1 > time2 else time2 - time1
        print('{:0>8}'.format(str(delta)))


main(sys.argv[1])
