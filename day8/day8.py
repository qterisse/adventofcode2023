with open("day8_input") as f:
	lines = f.read().split('\n')

def part1():
	def find_node(letters):
		for node in range(2, len(lines)):
			if (lines[node][:3] == letters):
				return (node)

	count = 0
	instructions = lines[0]
	current_node = find_node('AAA')
	while (lines[current_node].split(' ')[0] != 'ZZZ'):
		next_nodes = lines[current_node].split("(")[-1][:-1].split(", ")
		current_node = find_node(next_nodes[int(instructions[count % len(instructions)] == 'R')])
		count += 1
	
	print(f"It took {count} steps to go to ZZZ")

def part2():
	connections = {}
	for line in lines[2:]:
		a = line.split(' ')[0]
		b = line.split("(")[-1][:-1].split(", ")[0]
		c = line.split("(")[-1][:-1].split(", ")[1]
		connections[a] = (b, c)

	def find_end(start:str):
		steps = 0
		while(not start.endswith('Z')):
			start = connections[start][lines[0][steps % len(lines[0])] == 'R']
			steps += 1
		return (steps)
	
	def lcm(a, b):
		greater = max(a, b)
		smallest = min(a, b) 
		for i in range(greater, a*b+1, greater): 
			if i % smallest == 0: 
				return i 

	count = 1
	for node in connections:
		if (node.endswith('A')):
			count = lcm(count, find_end(node))
	print(f"It took {count} steps to go to only nodes ending with Z")

if __name__ == "__main__":
	part2()