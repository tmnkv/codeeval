import sys


cipher = dict(zip("abcdefghij", "0123456789"))
for line in open(sys.argv[1]):
    output = ""
    for symbol in line:
        if symbol.isdigit():
            output += str(symbol)
        if symbol in cipher:
            output += cipher[symbol]
    if output == "":
        output += "NONE"
    print(output)


