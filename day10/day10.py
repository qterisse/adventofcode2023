def part1():
	import matplotlib.path

	with open("day10_input") as f:
		lines = f.read().split('\n')

	pos = [0, 0]
	for y in range(len(lines)):
		for x in range(len(lines[y])):
			if (lines[y][x] == 'S'):
				pos = [x, y]
				break

	nodes = [tuple(pos)]
	pos[1] -= 1
	direction = [0, -1]
	while (lines[pos[1]][pos[0]] != 'S'):
		nodes.append(tuple(pos))
		if (lines[pos[1]][pos[0]] in '7FJL'):
			direction.reverse()
		if (lines[pos[1]][pos[0]] in 'JF'):
			direction = [d * -1 for d in direction]
		pos[0] += direction[0]
		pos[1] += direction[1]

	count = 0
	polygon = matplotlib.path.Path(nodes)
	nodes = set(nodes)
	for y in range(1, len(lines) - 1):
		for x in range(1, len(lines[y]) - 1):
			point = (y, x)
			if (polygon.contains_point(point) and point not in nodes):
				count += 1
	
	print(f"part1: {len(nodes) // 2}")
	print(f"part2: {count}")

if __name__ == "__main__":
	part1()