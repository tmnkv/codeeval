import sys


for line in open(sys.argv[1]):
    numbers = line.split()
    numbers = [int(x) for x in numbers]
    X, Y, N = numbers
    output = ""
    for i in range(1, N + 1):
        if i % X == 0 and i % Y == 0:
            output += "FB" + " "
        elif i % X == 0:
            output += "F" + " "
        elif i % Y == 0:
            output += "B" + " "
        else:
            output += str(i) + " "
    print(output)