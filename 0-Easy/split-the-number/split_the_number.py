import sys


def main(input_file):
    fh = open(input_file)
    for line in fh:
        number, template = line.rstrip().split()
        if '+' in template:
            index = template.index('+')
            result = int(number[:index]) + int(number[index:])
        if '-' in line:
            index = template.index('-')
            result = int(number[:index]) - int(number[index:])
        print(result)


main(sys.argv[1])
