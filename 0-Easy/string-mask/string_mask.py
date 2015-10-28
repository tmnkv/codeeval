import sys


for line in open(sys.argv[1]):
    word, mask = line.split()
    letters = ""
    for i in range(len(word)):
        if mask[i] == "1":
            letters += word[i].upper()
        else:
            letters += word[i]
    print(letters)