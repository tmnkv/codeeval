import sys
from math import sqrt


for line in open("input.txt"):
    elements = line.rstrip().split()
    N = int(sqrt(len(elements)))
    matrix = [elements[i * N:(i + 1) * N] for i in range(N)]
    clockwise_matrix = []
    for i in range(N):
        clockwise_matrix.append([matrix[x][i] for x in range(N)[::-1]])
    for i in range(N):
        print(" ".join(clockwise_matrix[i]), end=" ")
    print()
