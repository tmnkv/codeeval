import sys


for line in open(sys.argv[1]):
    letters = dict()
    for letter in line.rstrip().lower():
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    values = list(letters.values())
    values.sort(reverse=True)
    i = 26
    beauty = 0
    for value in values:
        beauty += i * value
        i -= 1
    print(beauty)