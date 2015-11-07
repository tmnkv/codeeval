import sys


for line in open(sys.argv[1]):
    sentence, code = line.split(";")
    words = sentence.split()
    numbers = code.split()
    words, code = [l.split() for l in line.split(";")]
    j = 0

    try:
        for i in range(1, len(words) + 1):
            j = numbers.index(str(i))
    except ValueError:
        numbers.append(str(i))

    line = ""
    for i in range(1, len(words) + 1):
        j = numbers.index(str(i))
        line += words[j] + " "
    print(line)