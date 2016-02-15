import sys


def main(input_file):
    fh = open(input_file, mode='r')
    for line in fh:
        line = [int(x) for x in line if x.isdigit()]
        total = sum(line) + sum(line[::2])
        result = 'Real' if total % 10 == 0 else 'Fake'
        print(result, total)


main(sys.argv[1])
