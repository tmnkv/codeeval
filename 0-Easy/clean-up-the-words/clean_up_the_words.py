import sys


for line in open(sys.argv[1]):
    text = ""
    flag = False
    for symbol in line:
        if symbol.isalpha():
            text += symbol.lower()
            flag = True
        elif not symbol.isalpha() and flag:
            text += " "
            flag = False
    print(text)
