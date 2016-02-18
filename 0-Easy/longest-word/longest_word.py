import sys


def main(input_file):
    fh = open(input_file)
    for line in fh:
        words = line.rstrip().split()
        lenght_of_words = [len(x) for x in words]
        position = lenght_of_words.index(max(lenght_of_words))
        print(words[position])


main(sys.argv[1])
