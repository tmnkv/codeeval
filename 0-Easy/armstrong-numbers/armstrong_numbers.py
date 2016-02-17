import sys


def main(input_file):
    fh = open(input_file)
    for number in fh:
        number = number.rstrip()
        armstrong = [int(x) ** len(number) for x in number]
        if int(number) == sum(armstrong):
            print("True")
        else:
            print('False')


main(sys.argv[1])
