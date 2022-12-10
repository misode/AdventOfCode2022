from collections import defaultdict

with open('day10/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]
	
	c = 1
	X = 1

	ROWS = 6
	COLS = 40
	D = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

	C = [20, 60, 100, 140, 180, 220]
	p1 = 0

	for line in lines:
		words = line.split(' ')
		
		if words[0] == 'noop':
			if abs(X - ((c-1) % COLS)) <= 1:
				D[(c-1) // COLS][(c-1) % COLS] = '█'
			c += 1
			if c in C:
				p1 += c * X
		elif words[0] == 'addx':
			if abs(X - ((c-1) % COLS)) <= 1:
				D[(c-1) // COLS][(c-1) % COLS] = '█'
			c += 1
			if c in C:
				p1 += c * X
			v = int(words[1])
			if abs(X - ((c-1) % COLS)) <= 1:
				D[(c-1) // COLS][(c-1) % COLS] = '█'
			c += 1
			X += v
			if c in C:
				p1 += c * X
	print(p1)
		
	print()
	for r in range(ROWS):
		for c in range(COLS):
			print(D[r][c], end='')
		print()
