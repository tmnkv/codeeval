import sys


def stupidSort(numbers, quantity):
    k = 0
    while k < len(numbers) - 1:
        if numbers[k] > numbers [k + 1]:
            tmp = numbers[k]
            numbers[k] = numbers[k + 1]
            numbers[k + 1] = tmp
            k = 0
            quantity -= 1
        else:
            k += 1
        if quantity == 0: break
    return numbers


def main(input_file):
    fh = open(input_file, mode='r')
    for line in fh:
        numbers, quantity = line.rstrip().split(' | ')
        quantity = int(quantity)
        numberss = [int(x) for x in numbers.split()]
        res = stupidSort(numberss, quantity)
        print("{2} :: {0} - {1}".format(numbers, " ".join([str(x) for x in res]), quantity))
    fh.close()


# if __name__ == '__main__':
#     if len(sys.argv) != 2:
#         print('Usage: {0} <input_file>'.format(sys.argv[0]))
#         sys.exit(1)
#     main(sys.argv[1])
main('/Users/tmnkv/GitHub/codeeval/0-Easy/not-so-clever/input.txt')
