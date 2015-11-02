import sys


for line in open(sys.argv[1]):
    words = line.rstrip().split()
    swap_words = []
    for word in words:
        swap_words.append(word[-1] + word[1:-1] + word[0])
    print(" ".join(swap_words))