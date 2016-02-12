import sys


def fillTheSet(data):
    teams = set()
    for i in range(len(data)):
        teams = teams.union({int(x) for x in data[i]})
    return teams


def fanSearch(team, data):
    result = []
    for number in range(len(data)):
        if str(team) in data[number]:
            result.append(str(number + 1))
    return result


def main(inpit_file):
    fh = open(inpit_file, mode='r')
    for line in fh:
        data = line.rstrip().split(' | ')
        data = [x.split() for x in data]
        teams = fillTheSet(data)
        for team in sorted(teams):
            fans = fanSearch(team, data)
            print('{0}:{1};'.format(team, ','.join(fans)), end=' ')
        print()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {0} <input_file>".format(sys.argv[0]))
    main(sys.argv[1])
