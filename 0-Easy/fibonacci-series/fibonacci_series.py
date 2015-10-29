import sys


def fibonacci(n):
    result = [0, 1]
    for i in range(2, n + 1):
        result.append(result[i - 2] + result[i - 1])
    return result

numbers = [int(i) for i in open(sys.argv[1])]
fibonaci_series = fibonacci(max(numbers))
for i in numbers:
    print(fibonaci_series[i])

