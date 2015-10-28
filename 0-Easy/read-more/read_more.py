__author__ = 'tmnkv'

for line in open("input.txt"):
    line = line.rstrip()
    if len(line) > 55:
        line = line[:40].rsplit(" ", 1)[0] + "... <Read More>"
    print(line)