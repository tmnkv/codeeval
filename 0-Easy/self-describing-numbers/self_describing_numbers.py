import sys


def self_subscribe(number, dct):
    for i in range(len(number)):
        if int(number[i]) != dct.get(str(i), 0):
            return 0
    return 1

def main(input_file):
    fh = open(input_file)
    for number in fh:
        number = number.rstrip()
        dct = {}
        for digit in number:
            dct[digit] = dct.get(digit, 0) + 1
        print(self_subscribe(number, dct))


main(sys.argv[1])
