from collections import deque
import re

with open('day19/in.txt') as f:
  lines = [l.strip() for l in f.readlines()]

  B = []

  for line in lines:
    m = re.match("Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.", line).groups()
    B.append(tuple(int(s) for s in m))

  for part1 in (True, False):

    T = 24 if part1 else 32
    ans = 0 if part1 else 1

    for id, ore_ore, clay_ore, ob_ore, ob_clay, geode_ore, geode_ob in B if part1 else B[:3]:
      max_ore = max([ore_ore, clay_ore, ob_ore, geode_ore])
      max_clay = ob_clay
      max_ob = geode_ob

      max_geodes = 0
      visited = set()
      Q = deque([(0, 0, 0, 0, 0, 1, 0, 0, 0)]) # start with one ore robot
      while Q:
        t, i1, i2, i3, i4, r1, r2, r3, r4 = Q.popleft()
        if i4 > max_geodes:
          max_geodes = i4
        if t >= T:
          continue

        # limit number of robots
        r1 = min(r1, max_ore)
        r2 = min(r2, max_clay)
        r3 = min(r3, max_ob)
        # limit number of items
        i1 = min(i1, 2*max_ore)
        i2 = min(i2, 2*max_clay)
        i3 = min(i3, 2*max_ob)
        u = t, i1, i2, i3, i4, r1, r2, r3, r4
        if u in visited:
          continue
        visited.add(u)

        Q.append((t+1,   i1+r1,           i2+r2,         i3+r3,          i4+r4, r1, r2, r3, r4))
        if i1 >= ore_ore:
          Q.append((t+1, i1+r1-ore_ore,   i2+r2,         i3+r3,          i4+r4, r1+1, r2, r3, r4))
        if i1 >= clay_ore:
          Q.append((t+1, i1+r1-clay_ore,  i2+r2,         i3+r3,          i4+r4, r1, r2+1, r3, r4))
        if i1 >= ob_ore and i2 >= ob_clay:
          Q.append((t+1, i1+r1-ob_ore,    i2+r2-ob_clay, i3+r3,          i4+r4, r1, r2, r3+1, r4))
        if i1 >= geode_ore and i3 >= geode_ob:
          Q.append((t+1, i1+r1-geode_ore, i2+r2,         i3+r3-geode_ob, i4+r4, r1, r2, r3, r4+1))

      if part1:
        ans += id * max_geodes
      else:
        ans *= max_geodes

    print(ans)
