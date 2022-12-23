with open('day01/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]

	p1 = 0
	elves = []
	cur = 0
	i = 0
	while i < len(lines):
		if len(lines[i]) == 0:
			elves.append(cur)
			p1 = max(p1, cur)
			cur = 0
		else:
			cur += int(lines[i])
		i += 1
	elves.append(cur)

	elves.sort()
	print(p1)
	print(elves[-1] + elves[-2] + elves[-3])
