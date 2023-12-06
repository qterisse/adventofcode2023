def part1():
	with open("day5_input") as f:
		lines = f.read().split('\n')
	
	values = [int(seed) for seed in lines[0].split(':')[-1].strip().split(' ')]
	order = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
	step = 1
	while (step < len(order)):
		start_index = lines.index(order[step - 1] + "-to-" + order[step] + " map:")
		for val_index in range(len(values)):
			i = start_index + 1
			value = values[val_index]
			while (i < len(lines) and len(lines[i]) and lines[i][0] in "0123456789"):
				map_range = [int(elem) for elem in lines[i].split(' ')]
				if (value >= map_range[1] and value < map_range[1] + map_range[2]):
					values[val_index] = map_range[0] + (value - map_range[1])
					break
				i += 1
		step += 1

	print(f'min value: {min(values)}') # correct answer: 265018614

def value_in_seeds(value, seeds):
	for n in range(1, len(seeds), 2):
		if (value >= seeds[n - 1] and value < seeds[n - 1] + seeds[n]):
			return True
	return False

def part2():
	with open("day5_input") as f:
		lines = f.read().split('\n')
	
	min_location = 0
	try:
		with open("saved_data") as f:
			min_location = int(f.read())
	except:
		print("No saved data")
	
	seeds = [int(seed) for seed in lines[0].split(':')[-1].strip().split(' ')]
	order = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
	order.reverse()

	almanac = [] # [[[], []], [[], []], [[], []]]
	for step in range(1, len(order)):
		step_maps = []
		i = lines.index(order[step] + "-to-" + order[step - 1] + " map:") + 1
		while (i < len(lines) and len(lines[i]) and lines[i][0] in "0123456789"):
			step_maps.append([int(elem) for elem in lines[i].split(' ')])
			i += 1
		almanac.append(step_maps[:])
	
	value = -1
	print("Loading ", end='', flush=True)
	try:
		while (value == -1 or not value_in_seeds(value, seeds)):
			step = 0
			value = min_location
			if (value % 1_000_000 == 0):
				print('.', end='', flush=True)
			for n, step in enumerate(almanac):
				for map_range in step:
					if (value >= map_range[0] and value < map_range[0] + map_range[2]):
						value = map_range[1] + (value - map_range[0])
						break
			min_location += 1
	except:
		print(f"\nStopped at {min_location}.\nSaved in 'saved_data' file")
		with open("saved_data", 'w') as fw:
			fw.write(str(min_location))
		return

	print(f'\n\nmin location found: {min_location} (seed: {value})') # 63_179_500

if __name__ == "__main__":
	part2()