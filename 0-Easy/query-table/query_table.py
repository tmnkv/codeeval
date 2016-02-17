import sys

N = 256


def create_matrix(fill=0):
    M = []
    v = [fill] * N
    for i in range(N):
        M.append(v)
    return M


def set_row(M, i, fill):
    v = [fill] * N
    M[i] = v
    return M


def set_col(M, j, fill):
    for i in range(N):
        M[i][j] = fill
    return M


def query_row(M, i):
    return sum(M[i])


def query_col(M, j):
    return sum([M[i][j] for i in range(N)])


def main(input_file):
    Matrix = create_matrix()
    fh = open(input_file)
    for line in fh:
        query, *param = line.rstrip().split()
        param = [int(x) for x in param]
        if query == 'SetRow':
            Matrix = set_row(Matrix, *param)
        elif query == 'SetCol':
            Matrix = set_col(Matrix, *param)
        elif query == 'QueryRow':
            print(query_row(Matrix, *param))
        elif query == 'QueryCol':
            print(query_col(Matrix, *param))


main(sys.argv[1])
