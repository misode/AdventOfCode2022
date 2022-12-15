import re
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
  x: int
  y: int
  def dist(self, other: "Point"):
    return abs(self.x - other.x) + abs(self.y - other.y)
  def rotate(self):
    return Point(self.x + self.y, self.y - self.x)
  def unrotate(self):
    return Point(round(self.x/2 - self.y/2), round(self.x/2 + self.y/2))

with open('day15/in.txt') as f:
  lines = [l.strip() for l in f.readlines()]

  P1_Y = 2000000
  P2_MAX = 4000000
  min_x = 0
  max_x = 0
  max_d = 0
  S = []
  B = set()

  for line in lines:
    a, b, c, d = [int(s) for s in re.match("Sensor at x=([\-\d]+), y=([\-\d]+): closest beacon is at x=([\-\d]+), y=([\-\d]+)", line).groups()]
    sensor = Point(a, b)
    beacon = Point(c, d)
    d = sensor.dist(beacon)
    min_x = min(sensor.x, min_x)
    max_x = max(sensor.x, max_x)
    max_d = max(d, max_d)
    c1 = Point(sensor.x-d, sensor.y).rotate()
    c2 = Point(sensor.x+d, sensor.y).rotate()
    c3 = Point(sensor.x, sensor.y-d).rotate()
    c4 = Point(sensor.x, sensor.y+d).rotate()
    x1 = min(c1.x, c2.x, c3.x, c4.x)
    x2 = max(c1.x, c2.x, c3.x, c4.x)
    y1 = min(c1.y, c2.y, c3.y, c4.y)
    y2 = max(c1.y, c2.y, c3.y, c4.y)
    S.append((x1, x2, y1, y2))
    B.add(beacon)

  p1 = 0
  i = min_x-max_d
  last = S[0]
  while i <= max_x+max_d:
    p = Point(i, P1_Y).rotate()
    if last[0] <= p.x <= last[1] and last[2] <= p.y <= last[3]:
      p1 += 1
      if last[0] <= (p.x+100) <= last[1] and last[2] <= (p.y-100) <= last[3]:
        p1 += 100
        i += 100
    else:
      for s in S:
        if s[0] <= p.x <= s[1] and s[2] <= p.y <= s[3]:
          last = s
          p1 += 1
          break
    i += 1
  beacons = len([b for b in B if b.y == P1_Y])
  print(p1 - beacons)

  y = min([s[2] for s in S])
  p2 = None
  while not p2:
    overlap_y = [s for s in S if s[2] <= y <= s[3]]
    if not overlap_y:
      break
    x = min([s[0] for s in overlap_y])
    while not p2:
      overlap_x = [o for o in overlap_y if o[0] <= x <= o[1]]
      if not overlap_x:
        rotated = Point(x, y).unrotate()
        if rotated.x <= P2_MAX and rotated.y < P2_MAX:
          p2 = rotated.x * 4000000 + rotated.y
        break
      x = max([o[1] for o in overlap_x]) + 1
    y = min([s[3] for s in overlap_y]) + 1

  print(p2)
