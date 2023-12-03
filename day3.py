def check_neighbours(lines, row, col, nrow, ncol):
	for n in range(-1 * (row != 0), (1 * (row != nrow - 1)) + 1):
		for i in range(-1 * (col != 0), (1 * (col != ncol - 1)) + 1):
			if (not lines[row + n][col + i] in "0123456789."):
				return 1
	return 0

def part1():
	with open("day3_input") as f:
		lines = f.read().split('\n')
	
	total = 0
	for row in range(len(lines)):
		end = -1
		for col in range(len(lines[row])):
			elem = lines[row][col]
			if ((col < end) or (not elem in "0123456789")):
				continue
			if (elem in "0123456789"):
				start, end, valid = col, col, False
				while (end < len(lines[row]) and lines[row][end] in "0123456789"):
					if (check_neighbours(lines, row, end, len(lines), len(lines[row]))):
						valid = True
					end += 1
				if (valid):
					total += int(lines[row][start:end])
	
	print(f'result: {total}')

def gear_product(lines, row, col, nrow, ncol):
	product, count = 1, 0
	for n in range(-1 * (row != 0), (1 * (row != nrow - 1)) + 1):
		end = -1
		for i in range(-1 * (col != 0), (1 * (col != ncol - 1)) + 1):
			if (col + i < end):
				continue
			if (lines[row + n][col + i] in "0123456789" and count == 2):
				return 0
			if (lines[row + n][col + i] in "0123456789"):
				start, end = col + i, col + i
				while (start >= 0 and lines[row + n][start] in "0123456789"):
					start -= 1
				while (end < ncol and lines[row + n][end] in "0123456789"):
					end += 1
				product *= int(lines[row + n][start + 1:end])
				count += 1
	if (count != 2):
		return 0
	return product

def part2():
	with open("day3_input") as f:
		lines = f.read().split('\n')

	total = 0
	for row in range(len(lines)):
		for col in range(len(lines[row])):
			elem = lines[row][col]
			if (elem == '*'):
				product = gear_product(lines, row, col, len(lines), len(lines[row]))
				if (row == 14):
					print(f'{product} from the gear at {row},{col}')
				total += product

	print(f'result: {total}')

def main():
	part2()

if __name__ == "__main__":
	main()