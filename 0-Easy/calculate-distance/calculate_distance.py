import sys
import re
from math import sqrt


def main(input_file):
    fh = open(input_file)
    for line in fh:
        p = re.compile('-?\d+')
        points = p.findall(line)
        x1, y1, x2, y2 = [int(x) for x in points]
        distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print(int(distance)


main(sys.argv[1])
