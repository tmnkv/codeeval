import sys


def without_repetitions(line):
    last = ""
    result = ""
    for letter in line:
        if letter != last:
            result += letter
            last = letter
    return result


def main(input_file):
    fh = open(input_file, "r")
    for line in fh:
        res = without_repetitions(line.rstrip())
        print(res)
    fh.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {0} <input_file>".format(sys.argv[0]))
        sys.exit(1)
    main(sys.argv[1])
