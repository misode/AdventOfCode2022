from collections import deque, defaultdict, Counter
import json, re, math, time
from dataclasses import dataclass
from functools import cache, lru_cache

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

with open('day24/in.txt') as f:
  lines = [l.strip() for l in f.readlines()]

  H = len(lines)
  W = len(lines[0])
  G = set()
  B = defaultdict(list)
  for r in range(H):
    for c in range(W):
      if lines[r][c] == '#':
        G.add((c, r))
      if lines[r][c] in "^>v<":
        B[(c, r)].append("^>v<".index(lines[r][c]))

  START = next((x, 0) for x in range(len(lines[0])) if (x, 0) not in G)
  END = next((x, H-1) for x in range(len(lines[0])) if (x, H-1) not in G)

  @cache
  def bliz(t: int) -> dict:
    if t == 0:
      return B
    P = bliz(t-1)
    P1 = defaultdict(list)
    for pos, l in P.items():
      for b in l:
        d = DIRS[b]
        x = pos[0]+d[0]
        y = pos[1]+d[1]
        if x <= 0:
          x = W-2
        if x >= W-1:
          x = 1
        if y <= 0:
          y = H-2
        if y >= H-1:
          y = 1
        P1[(x, y)].append(b)
    return P1

  back = False
  again = False

  Q = deque([(START, 0)])
  SEEN = set()
  while Q:
    u = Q.popleft()
    if u in SEEN:
      continue
    SEEN.add(u)
    pos, t = u
    if not back and pos == END:
      print(t)
      back = True
      Q = deque([(pos, t+1)])
      continue
    if back and not again and pos == START:
      again = True
      Q = deque([(pos, t+1)])
      continue
    if back and again and pos == END:
      print(t)
      break
    blizz = bliz(t+1)
    if pos not in blizz:
      Q.append((pos, t+1))
    for dx, dy in DIRS:
      target = pos[0]+dx, pos[1]+dy
      if target not in G and target not in blizz and target[1] >= 0 and target[1] < H:
        Q.append((target, t+1))
