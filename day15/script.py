import re
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
	x: int
	y: int
	def dist(self, other: "Point"):
		return abs(self.x - other.x) + abs(self.y - other.y)

with open('day15/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]

	min_x = 0
	max_x = 0
	max_d = 0

	S = []
	B = []

	for line in lines:
		a, b, c, d = [int(s) for s in re.match("Sensor at x=([\-\d]+), y=([\-\d]+): closest beacon is at x=([\-\d]+), y=([\-\d]+)", line).groups()]
		sensor = Point(a, b)
		beacon = Point(c, d)
		d = sensor.dist(beacon)
		min_x = min(sensor.x, min_x)
		max_x = max(sensor.x, max_x)
		max_d = max(d, max_d)
		S.append((sensor, d))
		B.append(beacon)

	p1 = 0
	Y = 2000000
	print(min_x - max_d)
	print(max_x + max_d + 1)
	for x in range(min_x - max_d, max_x + max_d + 1):
		p = Point(x, Y)
		if p in B:
			continue
		for s, d in S:
			if p.dist(s) <= d:
				p1 += 1
				break
	print(p1)
