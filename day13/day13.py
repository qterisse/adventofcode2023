def is_mirror(pattern, index):
	for n, line in enumerate(pattern[index+1:]):
		if (n > index):
			break
		if (pattern[index - n] != line):
			return (0)
	return (1)

def can_be_mirror(pattern, index):
	smudge_found = False
	for n, line in enumerate(pattern[index+1:]):
		if (n > index):
			break
		differences = [i for i in range(len(line)) if line[i] != pattern[index - n][i]]
		if (len(differences) > 1 or (smudge_found and len(differences) == 1)):
			return (0)
		elif (not smudge_found and len(differences) == 1):
			smudge_found = True
	return (smudge_found)

def rotate_pattern(pattern):
	rpattern = []
	for n in range(len(pattern[0])):
		rline = []
		for i in range(len(pattern)):
			rline.append(pattern[i][n])
		rpattern.append(''.join(rline[:]))
	return (rpattern)

def main(part=1):
	with open("day13_input") as f:
		patterns = [pattern.split('\n') for pattern in f.read().split('\n\n')]

	total = 0
	for i, pattern in enumerate(patterns):
		for h in [100, 1]:
			if (h == 1):
				pattern = rotate_pattern(pattern)
			found = False
			for n in range(len(pattern) - 1):
				if (part == 1):
					mirror = is_mirror(pattern, n)
				else:
					mirror = can_be_mirror(pattern, n)
				if (mirror):
					total += (n + 1) * h
					print(f'patterns[{i}] = {(n + 1) * h}')
					found = True
					break
			if (found):
				break

	print (f'part{part}: {total}')

if __name__ == "__main__":
	main(2)