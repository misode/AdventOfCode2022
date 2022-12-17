SHAPES = [
  [(0, 0), (1, 0), (2, 0), (3, 0)],
  [(0, 1), (1, 1), (2, 1), (1, 0), (1, 2)],
  [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
  [(0, 0), (0, 1), (0, 2), (0, 3)],
  [(0, 0), (0, 1), (1, 0), (1, 1)],
]

with open('day17/in.txt') as f:
  lines = [l.strip() for l in f.readlines()]
  PATTERN: str = lines[0]

  WORLD: set[tuple[int, int]] = set()

  def move(shape: list[tuple[int, int]], dx: int, dy: int):
    return [(p[0] + dx, p[1] + dy) for p in shape]

  def try_move(shape: list[tuple[int, int]], dx: int, dy: int):
    attempt = move(shape, dx, dy)
    for p in attempt:
      if p in WORLD:
        return False
      if p[0] < 0 or p[0] >= 7:
        return False
      if p[1] <= 0:
        return False
    return attempt

  J = dict()
  P2 = 1000000000000
  top = 0
  add_top = 0
  j = 0
  i = 0

  while i < P2:
    shape = SHAPES[i % len(SHAPES)]
    shape = move(shape, 2, top + 4)

    while True:
      jet_dir = -1 if PATTERN[j % len(PATTERN)] == "<" else 1
      j += 1
      shape2 = try_move(shape, jet_dir, 0)
      if shape2 != False:
        shape = shape2
      shape3 = try_move(shape, 0, -1)
      if shape3 != False:
        shape = shape3
      else:
        bottom = min([p[1] for p in shape])
        if i > 10000 and bottom > top and add_top == 0:
          jp = j % len(PATTERN)
          if jp in J:
            prev_top, prev_i = J[jp]
            if i % len(SHAPES) == prev_i & len(SHAPES):
              loop_length = i - prev_i
              height_size = top - prev_top
              repeats = (P2-i)//loop_length
              i += repeats * loop_length
              add_top = repeats * height_size
          J[jp] = (top, i)
        for p in shape:
          WORLD.add(p)
          if p[1] > top:
            top = p[1]
        i += 1
        if i == 2022:
          print(top)
        break

  print(top + add_top)
