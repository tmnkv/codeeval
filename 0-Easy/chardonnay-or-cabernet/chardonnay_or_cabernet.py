import sys


for line in open(sys.argv[1]):
    title, sub = line.rstrip().split(" | ")
    grades = title.split()
    output = []
    for grade in grades:
        flag = True
        original = grade
        for letter in sub.lower():
            if letter not in grade.lower():
                flag = False
                break
            grade = grade.replace(letter, "", 1)
        if flag:
            output.append(original)
    if output != []:
        print(" ".join(output))
    else:
        print("False")