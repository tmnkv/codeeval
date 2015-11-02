import sys


for line in open(sys.argv[1]):
    vampires, zombies, witches, houses = [int(l.split(":")[1]) for l in line.rstrip().replace(" ", "").split(",")]
    candies = int((vampires * 3 + zombies * 4 + witches * 5) * houses / (vampires + zombies + witches))
    print(candies)