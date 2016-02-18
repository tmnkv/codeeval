import sys


def main(input_file):
    fh = open(input_file)
    for line in fh:
        result = ''
        for letter in line.rstrip():
            if letter.isalpha() and letter.isupper():
                letter = letter.lower()
            elif letter.isalpha() and letter.islower():
                letter = letter.upper()
            result += letter
        print(result)


main(sys.argv[1])
