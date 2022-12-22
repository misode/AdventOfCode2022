from collections import deque, defaultdict
import json, re, math, time
from dataclasses import dataclass

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

with open('day22/in.txt') as f:
  lines = [l.removesuffix('\n') for l in f.readlines()]

  imap, ipath = '\n'.join(lines).split('\n\n')
  cols = max([len(row) for row in imap.split('\n')])
  G = [list(row.ljust(cols)) for row in imap.split('\n')]
  path = [s if s.isalpha() else int(s) for s in re.findall('\d+|L|R', ipath)]

  def wrap_flat(r: int, c: int, dir: int):
    r = r % len(G)
    c = c % len(G[0])

    while G[r][c] == ' ':
      r = (r + DIRS[dir][0]) % len(G)
      c = (c + DIRS[dir][1]) % len(G[0])

    return (r, c, dir)

  def wrap_cube(r: int, c: int, dir: int):
    if r < 0 or c < 0 or r >= len(G) or c >= len(G[0]) or G[r][c] == ' ':
      #     ┌─A─┬─B─┐
      #     N   │   C
      #     ├───┼─D─┘
      #     M   E
      # ┌─L─┼───┤
      # K   │   F
      # ├───┼─G─┘
      # J   H
      # └─I─┘
      if 50 <= c < 100 and r == -1 and dir == 3: # A -> J
        dir = 0
        r = c - 50 + 150
        c = 0
      elif 100 <= c < 150 and r == -1 and dir == 3: # B -> I
        dir = 3
        c = c - 100
        r = 199
      elif 0 <= r < 50 and c == 150 and dir == 0: # C -> F
        dir = 2
        r = 49 - r + 100
        c = 99
      elif 100 <= c < 150 and r == 50 and dir == 1: # D -> E
        dir = 2
        r = c - 100 + 50
        c = 99
      elif 50 <= r < 100 and c == 100 and dir == 0: # E -> D
        dir = 3
        c = r - 50 + 100
        r = 49
      elif 100 <= r < 150 and c == 100 and dir == 0: # F -> C
        dir = 2
        r = 99 - r + 50
        c = 149
      elif 50 <= c < 100 and r == 150 and dir == 1: # G -> H
        dir = 2
        r = c - 50 + 150
        c = 49
      elif 150 <= r < 200 and c == 50 and dir == 0: # H -> G
        dir = 3
        c = r - 150 + 50
        r = 149
      elif 0 <= c < 50 and r == 200 and dir == 1: # I -> B
        dir = 1
        c = c + 100
        r = 0
      elif 150 <= r < 200 and c == -1 and dir == 2: # J -> A
        dir = 1
        c = r - 150 + 50
        r = 0
      elif 100 <= r < 150 and c == -1 and dir == 2: # K -> N
        dir = 0
        r = 149 - r
        c = 50
      elif 0 <= c < 50 and r == 99 and dir == 3: # L -> M
        dir = 0
        r = c + 50
        c = 50
      elif 50 <= r < 100 and c == 49 and dir == 2: # M -> L
        dir = 1
        c = r - 50
        r = 100
      elif 0 <= r < 50 and c == 49 and dir == 2: # N -> K
        dir = 0
        r = 49 - r + 100
        c = 0
      else:
        assert False, (r, c, dir)
    return (r, c, dir)

  for wrapper in (wrap_flat, wrap_cube):
    r = 0
    c = G[0].index('.')
    dir = 0
    for step in path:
      if step == 'L':
        dir = (dir - 1) % 4
      elif step == 'R':
        dir = (dir + 1) % 4
      else:
        assert isinstance(step, int), step
        for i in range(step):
          tr = r + DIRS[dir][0]
          tc = c + DIRS[dir][1]
          tdir = dir

          tr, tc, tdir = wrapper(tr, tc, tdir)
          assert G[tr][tc] != ' '
          if G[tr][tc] == '#':
            break
          r, c, dir = tr, tc, tdir

    print(1000 * (r+1) + 4 * (c+1) + dir)
