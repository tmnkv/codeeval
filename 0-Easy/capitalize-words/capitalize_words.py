import sys


def main(input_file):
  fh = open(input_file)
  for line in fh:
    words = line.rstrip().split()
    words = [x[0].upper() + x[1:].lower() for x in words]
    print(' '.join(words))


main(sys.argv[1])
