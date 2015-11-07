import sys


for line in open(sys.argv[1], "r"):
    number = int(line.rstrip().split(";")[0])
    integers = [int(x) for x in line.rstrip().split(";")[1].split()]
    gain = 0
    for i in range(len(integers) - number + 1):
        gain = max(gain, sum(integers[i:i + number]))
    if gain <= 0:
        print("0")
    else:
        print(gain)
