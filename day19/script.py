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

  for line in lines:
    m = re.findall("Each ([a-z]+) robot costs ([^\.]*)\.", line)
    R: dict[str, dict[str, int]] = dict()
    for r, costs in m:
      R[r] = {k: int(cost) for cost, k in[i.split(' ') for i in costs.split(' and ')]}
    B.append(R)

  SUM = 0

  for id, blueprint in enumerate(B):

    max_ingredient = {k: max([r.get(k, 0) for r in blueprint.values()]) for k in ITEMS if k != "geode"}

    @lru_cache(maxsize=None)
    def next_states(state: State) -> list[State]:
      can_buy = []
      for robot, recipe in blueprint.items():
        if robot != "geode" and state.robots[ITEMS.index(robot)] > max_ingredient[robot]:
          continue
        if state.items[0] >= recipe.get("ore", 0) and state.items[1] >= recipe.get("clay", 0) and state.items[2] >= recipe.get("obsidian", 0):
          can_buy.append(robot)
      new_items = tuple([state.items[i]+state.robots[i] for i in range(4)])
      for i, item in enumerate(ITEMS):
        if new_items[i] > 40 and item in can_buy:
          can_buy.remove(item)
      if "geode" in can_buy:
        new_states = []
      else:
        new_states = [State(new_items, state.robots)]
      for bought in can_buy[-2:]:
        new_states.append(State(
          items=tuple([count - blueprint[bought].get(ITEMS[i], 0) for i, count in enumerate(new_items)]),
          robots=tuple([state.robots[i] + (1 if item==bought else 0) for i, item in enumerate(ITEMS)]),
        ))
      return new_states

    t0 = time.perf_counter()
    states = set([State((0,0,0,0), (1,0,0,0))])
    print(f'=== {id+1} ========')
    for m in range(24):
      new_states: set[State] = set()
      for s in states:
        for n in next_states(s):
          new_states.add(n)
      states = new_states
      if m > 15:
        t2 = time.perf_counter()
        print(m, len(states), f"{round(t2-t0)}s", next_states.cache_info())

    M = max([(id+1) * s.items[-1] for s in states])
    t1 = time.perf_counter()
    SUM += M
    print(f"  quality={M} sum={SUM} time={round(t1-t0)}s")

  print('!!!!', SUM)
