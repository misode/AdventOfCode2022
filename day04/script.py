
with open('day04/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]
	p1 = 0
	p2 = 0

	for line in lines:
		[a, b] = line.split(',')
		[a1, a2] = [int(n) for n in a.split('-')]
		[b1, b2] = [int(n) for n in b.split('-')]
		if (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2):
			p1 += 1
		if (a2 >= b1 and a1 <= b2) or (a1 <= b2 and a2 >= b1):
			p2 += 1

	print(p1)
	print(p2)
