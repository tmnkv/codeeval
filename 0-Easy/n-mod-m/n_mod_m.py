import sys


def main(input_file):
    fh = open(input_file)
    for line in fh:
        n,m = [int(x) for x in line.rstrip().split(',')]
        print(n % m)


main(sys.argv[1])
