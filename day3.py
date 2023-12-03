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

def main():
	part1()

if __name__ == "__main__":
	main()