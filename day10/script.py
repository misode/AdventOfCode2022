from collections import defaultdict

with open('day10/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]
	
	cycle = 0
	wait = 0
	wait_v = None
	x = 1
	signals = 0

	ROWS = 6
	COLS = 40
	display = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

	while lines:
		if cycle in [20, 60, 100, 140, 180, 220]:
			signals += cycle * x
		if abs(x - ((cycle-1) % COLS)) <= 1:
			display[(cycle-1) // COLS][(cycle-1) % COLS] = '█'

		cycle += 1
		if wait > 0:
			wait -= 1
		else:
			if wait_v is not None:
				x += wait_v
				wait_v = None
			line = lines[0].split(' ')
			lines = lines[1:]
			if line[0] == 'addx':
				wait_v = int(line[1])
				wait = 1
	
	print(signals)

	print()
	for r in range(ROWS):
		for c in range(COLS):
			print(display[r][c], end='')
		print()
