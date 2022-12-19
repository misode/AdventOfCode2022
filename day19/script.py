from collections import deque
import re
import time
from dataclasses import dataclass
from functools import lru_cache

DIRS = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
ITEMS = ["ore", "clay", "obsidian", "geode"]

@dataclass(frozen=True,eq=True)
class State:
  items: tuple[int, int, int, int]
  robots: tuple[int, int, int, int]

with open('day19/in.txt') as f:
  lines = [l.strip() for l in f.readlines()]

  B: list[dict[str, dict[str, int]]] = []

  for line in lines[:3]:
    m = re.findall("Each ([a-z]+) robot costs ([^\.]*)\.", line)
    R: dict[str, dict[str, int]] = dict()
    for r, costs in m:
      R[r] = {k: int(cost) for cost, k in[i.split(' ') for i in costs.split(' and ')]}
    B.append(R)

  T = 32
  ans = 1

  for id, blueprint in enumerate(B):

    b_ore_ore = blueprint["ore"]["ore"]
    b_clay_ore = blueprint["clay"]["ore"]
    b_ob_ore = blueprint["obsidian"]["ore"]
    b_ob_clay = blueprint["obsidian"]["clay"]
    b_geode_ore = blueprint["geode"]["ore"]
    b_geode_ob = blueprint["geode"]["obsidian"]
    max_ore = max([b_ore_ore, b_clay_ore, b_ob_ore, b_geode_ore])
    max_clay = b_ob_clay
    max_ob = b_geode_ob

    t0 = time.perf_counter()
    geodes = 0
    CACHE = set()
    Q = deque([(0, 0, 0, 0, 0, 1, 0, 0, 0)])
    while Q:
      t, i1, i2, i3, i4, r1, r2, r3, r4 = Q.popleft()
      if i4 > geodes:
        geodes = i4
      if t >= T:
        continue
      r1 = min(r1, max_ore)
      r2 = min(r2, max_clay)
      r3 = min(r3, max_ob)

      i1 = min(i1, (T-t)*max_ore-r1*(T-t-1))
      i2 = min(i2, (T-t)*max_clay-r2*(T-t-1))
      i3 = min(i3, (T-t)*max_ob-r3*(T-t-1))

      u = t, i1, i2, i3, i4, r1, r2, r3, r4
      if u in CACHE:
        continue
      CACHE.add(u)
      if len(CACHE) % 100000 == 0:
        print(t, geodes, len(CACHE), i1, i2, i3, i4, '|', r1, r2, r3, r4)

      Q.append((t+1, i1+r1, i2+r2, i3+r3, i4+r4, r1, r2, r3, r4))
      if i1 >= b_ore_ore:
        Q.append((t+1, i1+r1-b_ore_ore, i2+r2, i3+r3, i4+r4, r1+1, r2, r3, r4))
      if i1 >= b_clay_ore:
        Q.append((t+1, i1+r1-b_clay_ore, i2+r2, i3+r3, i4+r4, r1, r2+1, r3, r4))
      if i1 >= b_ob_ore and i2 >= b_ob_clay:
        Q.append((t+1, i1+r1-b_ob_ore, i2+r2-b_ob_clay, i3+r3, i4+r4, r1, r2, r3+1, r4))
      if i1 >= b_geode_ore and i3 >= b_geode_ob:
        Q.append((t+1, i1+r1-b_geode_ore, i2+r2, i3+r3-b_geode_ob, i4+r4, r1, r2, r3, r4+1))

    t1 = time.perf_counter()
    print(f"==== {id+1}: {geodes} | {round(t1-t0)}s")
    ans *= geodes

  print("!!!!", ans)
