
with open('day03/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]
	p1 = 0
	p2 = 0

	def priority(a: set):
		c = list(a)[0]
		if c >= 'a' and c <= 'z':
			return ord(c) - ord('a') + 1
		return ord(c) - ord('A') + 27

	for line in lines:
		n = len(line) // 2
		first = set(line[:n])
		second = set(line[n:])
		p1 += priority(first.intersection(second))

	for i in range(0, len(lines), 3):
		first = set(lines[i])
		second = set(lines[i+1])
		third = set(lines[i+2])
		p2 += priority(first.intersection(second).intersection(third))

	print(p1)
	print(p2)
