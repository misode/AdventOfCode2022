from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Point:
	x: int
	y: int


def dbg(rope: list[Point]):
	print('======')
	x0 = min([p.x for p in rope]) - 5
	y0 = min([p.y for p in rope]) - 5
	x1 = max([p.x for p in rope]) + 5
	y1 = max([p.y for p in rope]) + 5
	for y in range(y0, y1+1): 
		for x in range(x0, x1+1):
			index = [i for (i, p) in enumerate(rope) if p.x == x and p.y == y]
			if len(index) == 0:
				print('.', end='')
			else:
				if index[0] == 0:
					print('H', end='')
				else:
					print(index[0], end='')
		print()


with open('day09/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]

	for length in [2, 10]:
		rope = [Point(0, 0) for _ in range(length)]
		places = defaultdict(int)

		for line in lines:
			[d, s] = line.split(' ')
			s = int(s)
			dir = {
				"R": (1, 0),
				"L": (-1, 0),
				"D": (0, 1),
				"U": (0, -1),
			}[d]

			for j in range(s):
				rope[0].x += dir[0]
				rope[0].y += dir[1]

				for i, p in enumerate(rope[1:]):
					lead = rope[i]
					if abs(p.x - lead.x) <= 1 and abs(p.y - lead.y) <= 1:
						pass
					elif p.x == lead.x or p.y == lead.y:
						if p.x < lead.x - 1:
							p.x += 1
						elif p.x > lead.x + 1:
							p.x -= 1
						elif p.y < lead.y - 1:
							p.y += 1
						elif p.y > lead.y + 1:
							p.y -= 1
					else:
						if p.x < lead.x:
							p.x += 1
						else:
							p.x -= 1
						if p.y < lead.y:
							p.y += 1
						else:
							p.y -= 1

				tail = rope[-1]
				places[(tail.x, tail.y)] += 1
			# dbg(rope)

		print(len(places))
