import sys


def deci2sexa(deci):
    result = []
    for i in range(3):
        result.append(int(deci // 1))
        deci = (deci % 1) * 60
    return result


def main(input_file):
    fh = open(input_file)
    for line in fh:
        deci = float(line.rstrip())
        sexa = deci2sexa(deci)
        print('{0}.{1:0>2}\'{2:0>2}"'.format(*sexa))


main(sys.argv[1])
