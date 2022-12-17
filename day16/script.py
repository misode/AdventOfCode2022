import re
import time


with open('day16/in.txt') as f:
  lines = [l.strip() for l in f.readlines()]

  START = "AA"
  MAXT = 30
  V: dict[str, (int, list[str])] = dict()

  for line in lines:
    a, b, c = re.match("Valve (.+) has flow rate=(.+); tunnels? leads? to valves? (.*)", line).groups()
    V[a] = (int(b), c.split(', '))

  G: dict[str, list[(str, int)]] = dict()

  for a in V:
    if a != START and V[a][0] == 0:
      continue
    ADJ = dict()
    Q = [(a, 0)]
    S = set(a)
    while Q:
      u, d = Q.pop(0)
      for v in V[u][1]:
        if v in S:
          continue
        S.add(v)
        if v == START or V[v][0] > 0:
          ADJ[v] = d+1
        Q.append((v, d+1))
    G[a] = [(k, ADJ[k]) for k in ADJ]

  def search(a: str, t: int, open: tuple[str]):
    if t > MAXT or len(open) == len(G):
      return 0
    best = 0
    for a2, d2 in G[a]:
      if a2 in open:
        continue
      b2 = search(a2, t+d2+1, (*open, a2))
      score = b2 + V[a2][0] * (MAXT - (t+d2))
      if score > best:
        best = score
    return best

  t0 = time.perf_counter()
  print(search(START, 1, ("AA",)))
  t1 = time.perf_counter()
  print(f"Took {round((t1-t0)*1000)} ms")
