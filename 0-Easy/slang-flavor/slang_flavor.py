import sys
import re

SLANG = [
    ", yeah!",
    ", this is crazy, I tell ya.",
    ", can U believe this?",
    ", eh?",
    ", aw yea.",
    ", yo.",
    "? No way!",
    ". Awesome!"
]


def main(input_file):
    fh = open(input_file)
    flag = False
    count = 0
    for line in fh:
        sentences = [x for x in re.split('[.?!]', line.rstrip()) if len(x) >0]
        result = ''
        for sentence in sentences:
            if flag:
                result += sentence + SLANG[count % len(SLANG)]
                count += 1
                flag = False
            else:
                result += sentence + line[line.index(sentence) + len(sentence)]
                flag = True
        print(result)




main(sys.argv[1])
