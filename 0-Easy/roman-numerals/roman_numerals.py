import sys

def exponent(exp):
    if exp == 1:
        return 'IVX'
    elif exp == 10:
        return 'XLC'
    elif exp == 100:
        return 'CDM'
    elif exp == 1000:
        return 'M'


def arabicToRoman(digit, letters):
    if digit == 0:
        return ''
    if letters == 'M':
        return digit * letters
    if 1 <= digit <= 3:
        return digit * letters[0]
    elif digit == 4:
        return letters[0] + letters[1]
    elif digit == 5:
        return letters[1]
    elif 6 <= digit <= 8:
        return letters[1] + (digit - 5) * letters[0]
    elif digit == 9:
        return letters[0] + letters[2]


def main(input_file):
    fh = open(input_file)
    for line in fh:
        roman = ''
        number = int(line)
        for i in (1000, 100, 10, 1):
            digit = number // i
            roman += str(arabicToRoman(digit, exponent(exp=i)))
            number = number % i
        print(roman)


main(sys.argv[1])
