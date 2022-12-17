import re
import time


with open('day16/in.txt') as f:
  lines = [l.strip() for l in f.readlines()]

  START = "AA"
  TIME_1 = 30
  TIME_2 = 26
  RATE: dict[str, int] = dict()
  TUNNELS: dict[str, list[str]] = dict()

  for line in lines:
    a, b, c = re.match("Valve (.+) has flow rate=(.+); tunnels? leads? to valves? (.*)", line).groups()
    RATE[a] = int(b)
    TUNNELS[a] = c.split(', ')

  G: dict[str, dict[str, int]] = dict()

  for a in TUNNELS:
    if a != START and RATE[a] == 0:
      continue
    ADJ: dict[str, int] = dict()
    Q = [(a, 0)]
    S = set(a)
    while Q:
      u, d = Q.pop(0)
      for v in TUNNELS[u]:
        if v in S:
          continue
        S.add(v)
        if v == START or RATE[v] > 0:
          ADJ[v] = d+1
        Q.append((v, d+1))
    G[a] = ADJ

  def search_1(a: str, t: int, open: tuple[str]):
    if t > TIME_1 or len(open) == len(G):
      return 0
    best = 0
    for a2, d2 in G[a].items():
      if a2 in open:
        continue
      b2 = search_1(a2, t+d2+1, (*open, a2))
      score = b2 + RATE[a2] * (TIME_1 - (t+d2))
      if score > best:
        best = score
    return best

  print(search_1(START, 1, (START,)))

  def search_2(a1: str, t1: int, a2: str, t2: int, open: tuple[str]):
    if t1 > TIME_2 or t2 > TIME_2 or len(open) == len(G):
      return 0
    best = 0
    for b, d in G[a1].items():
      if b in open:
        continue
      score = search_2(b, t1+d+1, a2, t2, (*open, b))
      total = score + RATE[b] * (TIME_2 - (t1+d))
      if total > best:
        best = total
    for b, d in G[a2].items():
      if b in open:
        continue
      score = search_2(a1, t1, b, t2+d+1, (*open, b))
      total = score + RATE[b] * (TIME_2 - (t2+d))
      if total > best:
        best = total
    return best

  t0 = time.perf_counter()
  print(search_2(START, 1, START, 1, (START,)))
  t1 = time.perf_counter()
  print(f"Took {round((t1-t0)*1000)} ms")
