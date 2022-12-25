from collections import deque, defaultdict, Counter
import json, re, math, time
from dataclasses import dataclass
from functools import cache, lru_cache

with open('day25/in.txt') as f:
  lines = [l.strip() for l in f.readlines()]

  def from_snafu(s: str):
    x = 0
    for i, c in enumerate(reversed(s)):
      x += (5**i) * {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}[c]
    return x

  def to_snafu(x: int):
    if x == 0:
      return "0"
    s = ''
    while x != 0:
      rem = x % 5
      s += {2: "2", 1: "1", 0: "0", 4: "-", 3: "="}[rem]
      x = x // 5 + (1 if rem > 2 else 0)
    return "".join(reversed(s))

  fuel = sum(from_snafu(l) for l in lines)
  print(to_snafu(fuel))
  assert from_snafu(to_snafu(fuel)) == fuel
