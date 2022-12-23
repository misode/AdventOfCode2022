from collections import deque, defaultdict, Counter
import json, re, math, time
from dataclasses import dataclass

with open('day23/in.txt') as f:
  lines = [l.strip() for l in f.readlines()]

  E = set()
  for r in range(len(lines)):
    for c in range(len(lines[0])):
      if lines[r][c] == '#':
        E.add((c, r))

  DIRS = [0, 1, 2, 3]

  for round in range(100000000):
    moves = dict()
    for x, y in E:
      empty = True
      for dx in range(-1, 2):
        for dy in range(-1, 2):
          if (x+dx, y+dy) != (x, y) and (x+dx, y+dy) in E:
            empty = False
      if empty:
        continue
      for d in DIRS:
        if d == 0 and (x-1, y-1) not in E and (x, y-1) not in E and (x+1, y-1) not in E:
          moves[(x, y)] = (x, y-1)
          break
        if d == 1 and (x-1, y+1) not in E and (x, y+1) not in E and (x+1, y+1) not in E:
          moves[(x, y)] = (x, y+1)
          break
        if d == 2 and (x-1, y-1) not in E and (x-1, y) not in E and (x-1, y+1) not in E:
          moves[(x, y)] = (x-1, y)
          break
        if d == 3 and (x+1, y-1) not in E and (x+1, y) not in E and (x+1, y+1) not in E:
          moves[(x, y)] = (x+1, y)
          break

    targets = Counter(moves.values())
    NE = set()
    for x, y in E:
      if (x, y) not in moves:
        NE.add((x, y))
      else:
        me = moves[(x, y)]
        if targets[me] > 1:
          NE.add((x, y))
        else:
          NE.add(me)
    
    if NE == E:
      print(round + 1)
      break

    E = NE
    DIRS = DIRS[1:] + [DIRS[0]]

    if round + 1 == 10:
      x1 = min([e[0] for e in E])
      x2 = max([e[0] for e in E])
      y1 = min([e[1] for e in E])
      y2 = max([e[1] for e in E])
      
      w = (x2-x1+1)
      h = (y2-y1+1)
      print(w*h - len(E))
