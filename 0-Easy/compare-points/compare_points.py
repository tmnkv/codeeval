import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

for line in open(sys.argv[1]):
    O, P, Q, R = [int(x) for c in line.rstrip().split()]
    current = Point(O, P)
    overlook = Point(Q, R)
    if current == overlook:
        print("here")
    elif current.x < overlook.x and current.y < overlook.y:
        print("NE")
    elif current.x > overlook.x and current.y < overlook.y:
        print("NW")
    elif current.x > overlook.x and current.y > overlook.y:
        print("SW")
    elif current.x < overlook.x and current.y > overlook.y:
        print("SE")
    elif current.x == overlook.x and current.y < overlook.y:
        print("N")
    elif current.x == overlook.x and current.y > overlook.y:
        print("S")
    elif current.x < overlook.x and current.y == overlook.y:
        print("E")
    elif current.x > overlook.x and current.y == overlook.y:
        print("W")

