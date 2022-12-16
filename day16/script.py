from collections import defaultdict
import re
from dataclasses import dataclass
import math
import time
from functools import lru_cache

@dataclass(frozen=True)
class Valve:
  id: str
  adj: list[str]
  rate: int


with open('day16/example.txt') as f:
  lines = [l.strip() for l in f.readlines()]

  V: dict[str, Valve] = dict()

  for line in lines:
    a, b, c = re.match("Valve (.+) has flow rate=(.+); tunnels? leads? to valves? (.*)", line).groups()
    V[a] = Valve(a, c.split(', '), int(b))

  @lru_cache(maxsize=None)
  def search(a: str, t: int, open: tuple[str]):
    if t > 30:
      return 0
    releasing = sum(V[id].rate for id in open)
    if len(open) == len(V):
      return releasing

    best = 0

    if a not in open:
      best = max([best, search(a, t+1, (*open, a))]) # open A

    for a2 in V[a].adj:
      best = max([best, search(a2, t+1, open)]) # move to A2

    return best + releasing

  t0 = time.perf_counter()
  print(search("AA", 1, ()))
  t1 = time.perf_counter()
  print(f"Took {round(t1-t0)} seconds")
