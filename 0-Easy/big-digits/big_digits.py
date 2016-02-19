import sys

EXAMPLE = """-**----*--***--***---*---****--**--****--**---**--
*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-
*--*---*---**---**--****-***--***----*---**---***-
*--*---*--*-------*----*----*-*--*--*---*--*----*-
-**---***-****-***-----*-***---**---*----**---**--
--------------------------------------------------"""
DIGITS = dict(zip('0123456789', [[],[],[],[],[],[],[],[],[],[]]))
for line in EXAMPLE.split('\n'):
    for i in range(10):
        DIGITS[str(i)].append(line.rstrip()[i*5:(i+1)*5])


def main(input_file):
  fh = open(input_file)
  for line in fh:
      digits_only = [x for x in line if x.isdigit()]
      for i in range(6):
          result = ''
          for digit in digits_only:
              result += DIGITS[digit][i]
          print(result)


main(sys.argv[1])
