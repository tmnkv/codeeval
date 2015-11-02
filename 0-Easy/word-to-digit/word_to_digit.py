import sys


digits = {"zero":0,
          "one":1,
          "two":2,
          "three":3,
          "four":4,
          "five":5,
          "six":6,
          "seven":7,
          "eight":8,
          "nine":9}
for line in open(sys.argv[1]):
    words = line.rstrip().split(";")
    for word in words:
        print(digits[word], end="")
    print()