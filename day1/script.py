with open('day1/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]

	elves = []
	cur = 0
	i = 0
	while i < len(lines):
		if len(lines[i]) == 0:
			elves.append(cur)
			cur = 0
		else:
			cur += int(lines[i])
		i += 1
	elves.append(cur)

	elves.sort()
	print(elves)
	print(elves[-1] + elves[-2] + elves[-3])
