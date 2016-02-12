import sys


def testing(line):
	bugs = 0
	test, example = line.rstrip().split(" | ")
	for i in range(len(test)):
		if test[i] != example[i]:
			bugs +=1
	if bugs == 0:
		return "Done"
	elif 0 < bugs <= 2:
		return "Low"
	elif 2 < bugs <= 4:
		return "Medium"
	elif 4 < bugs <= 6:
		return "High"
	else:
		return "Critical"


def main(input_file):
	fh = open(input_file, "r")
	for line in fh:
		res = testing(line)
		print(res)
	fh.close()


if __name__ == '__main__':
	# if len(sys.argv) != 2:
	# 	print("Usage: {0} <input_file>".format(sys.argv[0]))
	# 	sys.exit(1)
	# main(sys.argv[1])
	main("input.txt")