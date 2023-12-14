from functools import lru_cache

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd, flush=True)
    # Print New Line on Complete
    if iteration == total: 
        print()

def is_line_ok(line, groups):
	hash_groups = [e for e in line.split('.') if e]
	if (len(hash_groups) != len(groups)):
		return (0)
	for n, group in enumerate(hash_groups):
		if (groups[n] != len(group)):
			return (0)
	return (1)

def is_partial_line_ok(line, groups):
	hash_groups = [e for e in line.split('.') if e]
	if (len(hash_groups) > len(groups)):
		return (0)
	for n, group in enumerate(hash_groups):
		if (n != len(hash_groups) - 1 and groups[n] != len(group)):
			return (0)
	return (1)

@lru_cache(maxsize=None) 
def backtrack(line, groups, i):
	count = 0
	if (i == len(line) and is_line_ok(''.join(line), groups)):
		return (1)
	elif (i == len(line)):
		return (0)
	if (line[i] != '?'):
		return (backtrack(line, groups, i + 1))
	for n in '#.':
		line = line[:i] + n + line[i+1:]
		if (is_partial_line_ok(''.join(line)[:i], groups)):
			count += backtrack(line, groups, i + 1)
	return (count)

def part1():
	with open("day12_input") as f:
		ls = [l.split() for l in f.read().splitlines()]
	ls = [(p, tuple(int(n) for n in s.split(","))) for p, s in ls]

	print(sum(backtrack(p + ".", s, 0) for p, s in ls))

def part2():
	with open("day12_input") as f:
		lines = f.read().split('\n')
	
	total = 0
	for n, line in enumerate(lines):
		groups = [int(e) for e in line.split(' ')[1].split(',')]
		groups = [g for group in [groups for n in range(5)] for g in group]
		unfolded_line = '?'.join([line.split(' ')[0] for n in range(5)])
		total += backtrack(list(unfolded_line), groups, 0)
		printProgressBar(n, 1000)
	printProgressBar(1000, 1000)

	print(f"result: {total}")

if __name__ == "__main__":
	part1()