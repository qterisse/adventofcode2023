def main():
	with open("day11_input") as f:
		lines = f.read().split('\n')
	
	galaxies = set()

	true_y = 0
	for y in range(len(lines)):
		true_x = 0
		if (not '#' in lines[y]):
			true_y += 999999
		for x in range(len(lines[y])):
			if (lines[y][x] == '#'):
				galaxies.add((true_x, true_y))
			if (all([lines[h][x] == '.' for h in range(len(lines))])):
				true_x += 999999
			true_x += 1
		true_y += 1

	galaxies = sorted(galaxies, key=lambda x: (x[1], x[0]))

	def steps(g1, g2):
		return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

	total = 0
	for n in range(len(galaxies)):
		for i, galaxy in enumerate(galaxies[n:]):
			total += steps(galaxy, galaxies[n])

	print(f"result: {total}")

if __name__ == "__main__":
	main()