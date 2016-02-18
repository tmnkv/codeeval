import sys


def knight_moves(position):
    lowercase = 'abcdefgh'
    x, y = lowercase.index(position[0]) + 1, int(position[1])
    moves1 = [(i, j) for i in [x-2, x+2]
                     for j in [y-1, y+1]
                     if 0<i<9 if 0<j<9]
    moves2 = [(i, j) for i in [x-1, x+1]
                     for j in [y-2, y+2]
                     if 0<i<9 if 0<j<9]
    return [lowercase[i - 1] + str(j) for (i, j) in moves1 + moves2]


def main(input_file):
    fh = open(input_file)
    for line in fh:
        moves = knight_moves(line.rstrip())
        print(' '.join(sorted(moves)))


main(sys.argv[1])
