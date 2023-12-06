def part1():
	with open("day6_input") as f:
		lines = f.read().split("\n")
	
	total = 1
	times = [int(elem) for elem in list(filter(None, lines[0].split(' ')))[1:]]
	records = [int(elem) for elem in list(filter(None, lines[1].split(' ')))[1:]]
	for race_index in range(len(times)):
		count = 0
		for speed in range(1, times[race_index]):
			if (speed * (times[race_index] - speed) > records[race_index]):
				count += 1
		total *= count

	print(f"result: {total}")

def part2():
	with open("day6_input") as f:
		lines = f.read().split("\n")
	
	total = 0
	time = int(''.join(list(filter(None, lines[0].split(' ')))[1:]))
	record = int(''.join(list(filter(None, lines[1].split(' ')))[1:]))
	for speed in range(1, time):
		if (speed * (time - speed) > record):
			total += 1
	
	print(f"result: {total}")

if __name__ == "__main__":
	part2()