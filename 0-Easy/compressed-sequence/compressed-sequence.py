import sys


def compressed_sequence(line):
    numbers = line.rstrip().split()
    result = ""
    temp = numbers[0]
    quantity = 0
    for number in numbers:
        if number == temp:
            quantity += 1
            continue
        else:
            result += "{0} {1} ".format(quantity, temp)
            temp = number
            quantity = 1
    result += "{0} {1}".format(quantity, temp)
    return result


def main(input_file):
    fh = open(input_file, "r")
    for line in fh:
        res = compressed_sequence(line)
        print(res)
    fh.close()


# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage {0} <input_file>".format(sys.argv[0]))
#         sys.exit(1)
#     main(sys.argv[1])
main("input.txt")