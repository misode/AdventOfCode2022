from collections import deque, defaultdict
import json, re, math, time
from dataclasses import dataclass

with open('day22/in.txt') as f:
  lines = [l.removesuffix('\n') for l in f.readlines()]

  imap, ipath = '\n'.join(lines).split('\n\n')
  cols = max([len(row) for row in imap.split('\n')])
  G = [list(row.ljust(cols)) for row in imap.split('\n')]

  path = [s if s in ('R', 'L') else int(s) for s in re.findall('\d+|L|R', ipath)]

  r = 0
  c = G[0].index('.')
  dir = 0
  DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

  for step in path:
    if isinstance(step, int):
      for i in range(step):
        tr = (r + DIRS[dir][0]) % len(G)
        tc = (c + DIRS[dir][1]) % len(G[0])
        
        while G[tr][tc] == ' ':
          tr = (tr + DIRS[dir][0]) % len(G)
          tc = (tc + DIRS[dir][1]) % len(G[0])

        if G[tr][tc] == '.':
          r = tr
          c = tc
        else:
          assert G[tr][tc] == '#'
          break
    elif step == 'L':
      dir = (dir - 1) % 4
    elif step == 'R':
      dir = (dir + 1) % 4
    else:
      assert False, step

  print(r, c, dir)
  print(1000 * (r+1) + 4 * (c+1) + dir)
