def check_neighbours(lines, row, col, nrow, ncol):
	for n in range(-1 * (row != 0), (1 * (row != nrow - 1)) + 1):
		for i in range(-1 * (col != 0), (1 * (col != ncol - 1)) + 1):
			if (not lines[row + n][col + i] in "0123456789."):
				return 0
	return 1

def main():
	with open("day3_input.txt") as f:
		lines = f.read().split('\n')
	
	total = 0
	for row in range(len(lines)):
		end = -1
		for col in range(len(lines[row])):
			elem = lines[row][col]
			if ((col < end) or (not elem in "0123456789")):
				continue
			if (elem in "0123456789"):
				start, end, valid = col, col, True
				while (elem in "0123456789"):
					if (end == len(lines[row])):
						end += 1
						break
					elem = lines[row][end]
					if (valid and not check_neighbours(lines, row, end, len(lines), len(lines[row]))):
						valid = False
					end += 1
				if (valid):
					print(f'valid: {lines[row][start:end - 1]} at row {row}')
					total += int(lines[row][start:end - 1])
	
	print(f'result: {total}')

if __name__ == "__main__":
	main()