def part1():
	with open("day4_input") as f:
		lines = f.read().split('\n')
	
	total = 0
	for line in lines:
		winners = [int(elem) for elem in line.split(':')[-1].strip().split('|')[0].strip().split(' ') if elem]
		given = [int(elem) for elem in line.split(':')[-1].strip().split('|')[-1].strip().split(' ') if elem]
		card_result = len([elem for elem in given if elem in winners]) - 1
		if (card_result >= 0):
			total += 2 ** card_result
	
	print(f"result: {total}")

def process_line(lines, index):
	total = 1
	winners = [int(elem) for elem in lines[index].split(':')[-1].strip().split('|')[0].strip().split(' ') if elem]
	given = [int(elem) for elem in lines[index].split(':')[-1].strip().split('|')[-1].strip().split(' ') if elem]
	for n in range(len([elem for elem in given if elem in winners])):
		print(f'card {index + n}')
		if (index + n + 1 < len(lines)):
			total += process_line(lines, index + n + 1)
	return (total)

def part2():
	with open("day4_input") as f:
		lines = f.read().split('\n')
	
	total = 0
	for index in range(len(lines)):
		total += process_line(lines, index)
	
	print(f"result: {total}")

if __name__ == "__main__":
	part2()