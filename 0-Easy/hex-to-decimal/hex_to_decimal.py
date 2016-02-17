import sys


def main(input_file):
    fh = open(input_file)
    for line in fh:
        print(int(float.fromhex(line.rstrip())))


main(sys.argv[1])
