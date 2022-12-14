from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
	x: int
	y: int
	def down(self):
		return Point(self.x, self.y+1)
	def down_left(self):
		return Point(self.x-1, self.y+1)
	def down_right(self):
		return Point(self.x+1, self.y+1)

with open('day14/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]

	def simulate(part2: bool):
		part1 = not part2
		G: set[Point] = set()
		for line in lines:
			path = [Point(*tuple([int(x) for x in p.split(',')])) for p in line.split(' -> ')]
			for a, b in zip(path, path[1:]):
				assert a.x == b.x or a.y == b.y
				for x in range(min(a.x, b.x), max(a.x, b.x)+1):
					for y in range(min(a.y, b.y), max(a.y, b.y)+1):
						G.add(Point(x, y))

		bottom = max([p.y for p in G])
		if part2:
			bottom +=2

		i = 0
		done = False
		while not done:
			i += 1
			s = Point(500, 0)
			while True:
				if part1 and s.y > bottom:
					done = True
					break
				if part2 and s.down().y == bottom:
					G.add(s)
					break
				if s.down() not in G:
					s = s.down()
				elif s.down_left() not in G:
					s = s.down_left()
				elif s.down_right() not in G:
					s = s.down_right()
				else:
					G.add(s)
					break
			if part2 and Point(500, 0) in G:
				done = True
		return i-1 if part1 else i

	print(simulate(False))
	print(simulate(True))
