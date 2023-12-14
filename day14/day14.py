def rotate_map(map):
	rmap = []
	for n in range(len(map[0])):
		rline = []
		for i in range(len(map)):
			rline.append(map[i][n])
		rmap.append(rline[:])
	return (rmap)

def part1():
	with open("day14_input") as f:
		map = rotate_map(f.read().split('\n'))
	
	for line in map:
		for n, elem in enumerate(line):
			if (elem == 'O'):
				i = n - 1
				while (i >= 0 and line[i] == '.'):
					line[i + 1] = '.'
					line[i] = 'O'
					i -= 1

	total = 0
	for line in map:
		for n, elem in enumerate(line):
			if (elem == 'O'):
				total += len(line) - n
	
	print(f'part1: {total}')

def part2():
	with open("day14_input") as f:
		map = [list(e) for e in f.read().split('\n')]

	def print_map(map):
		for line in map:
			print(' '.join(line))
		print()

	def roll_west(rocks):
		for line in rocks:
			for n, elem in enumerate(line):
				if (elem == 'O'):
					i = n - 1
					while (i >= 0 and line[i] == '.'):
						line[i + 1] = '.'
						line[i] = 'O'
						i -= 1
		return (rocks)

	def roll_east(rocks):
		for line in rocks:
			for n in range(len(line) - 1, -1, -1):
				if (line[n] == 'O'):
					line[n] = '.'
					line[min(line[n:].index('#')  if '#' in line[n:] else len(line) - 1, line[n:].index('O') if 'O' in line[n:]  else len(line) - 1) - 1] = 'O'
		return (rocks)

	def roll_north(rocks):
		for col in range(len(rocks[0])):
			for row in range(len(rocks)):
				if (rocks[row][col] == 'O'):
					i = row - 1
					while (i >= 0 and rocks[i][col] == '.'):
						rocks[i + 1][col] = '.'
						rocks[i][col] = 'O'
						i -= 1
		return (rocks)

	def roll_south(rocks):
		for col in range(len(rocks[0])):
			for row in range(len(rocks) - 1, -1, -1):
				if (rocks[row][col] == 'O'):
					i = row + 1
					while (i < len(rocks) and rocks[i][col] == '.'):
						rocks[i - 1][col] = '.'
						rocks[i][col] = 'O'
						i += 1
		return (rocks)

	for n in range(1000):
		for roll in [roll_north, roll_west, roll_south, roll_east]:
			roll(map)
	print_map(map)
	
if __name__ == "__main__":
	part2()
