import sys


for line in open(sys.argv[1]):
    number_of_zeros, lenght = [int(l) for l in line.rstrip().split()]
    quantity = 0
    for i in range(1, lenght + 1):
        if bin(i).count("0", 2) == number_of_zeros:
            quantity += 1
    print(quantity)