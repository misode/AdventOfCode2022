import re
import time


with open('day16/in.txt') as f:
  lines = [l.strip() for l in f.readlines()]

  RATE: dict[int, int] = dict()
  TUNNELS: dict[int, list[str]] = dict()
  KEYS: dict[str, int] = dict()

  for i, line in enumerate(lines):
    a, b, c = re.match("Valve (.+) has flow rate=(.+); tunnels? leads? to valves? (.*)", line).groups()
    KEYS[a] = i
    RATE[i] = int(b)
    TUNNELS[i] = c.split(', ')

  START = KEYS["AA"]
  for i in TUNNELS:
    TUNNELS[i] = [KEYS[t] for t in TUNNELS[i]]

  DP = dict()
  def search(a: int, t: int, open: int, elephants: int):
    if t == 0:
      return 0 if elephants == 0 else search(START, 26, open, elephants - 1)
    key = (a, t, open, elephants)
    if key in DP:
      return DP[key]
    best = 0
    if RATE[a] > 0 and (open & (1 << a)) == 0:
      best = RATE[a] * (t-1) + max(best, search(a, t-1, open | (1 << a), elephants))
    for a2 in TUNNELS[a]:
      best = max(best, search(a2, t-1, open, elephants))
    DP[key] = best
    return best

  print(search(START, 30, 0, 0))
  print(search(START, 26, 0, 1))
