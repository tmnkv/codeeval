# import sys

CODE = {"A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        "0" : "-----",
        "1" : ".----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",
}

def decode(line):
    reverse_code = dict((v,k) for (k,v) in CODE.items())
    words = line.rstrip().split("  ")
    result = ""
    for word in words:
        letters = word.split()
        for letter in letters:
            result += reverse_code[letter]
        result += " "
    return result


def main(input_file):
    fh = open(input_file, "r")
    for line in fh:
        res = decode(line)
        print(res)


# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage {0} <input_file>".format(sys.argv[0]))
#         sys.exit(1)
#     main(sys.argv[1])
main("input.txt")
