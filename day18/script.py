DIRS = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

with open('day18/in.txt') as f:
  lines = [l.strip() for l in f.readlines()]
  
  C = set()
  for line in lines:
    p = tuple([int(c) for c in line.split(',')])
    C.add(p)

  x1 = min([c[0] for c in C])
  x2 = max([c[0] for c in C])
  y1 = min([c[1] for c in C])
  y2 = max([c[1] for c in C])
  z1 = min([c[2] for c in C])
  z2 = max([c[2] for c in C])

  p1 = 0
  p2 = 0
  for x, y, z in C:
    for dx, dy, dz in DIRS:
      n = (x+dx, y+dy, z+dz)
      if n in C:
        continue
      p1 += 1
      Q = [n]
      vis = set([n])
      while Q:
        ux, uy, uz = Q.pop(0)
        if ux < x1 or ux > x2 or uy < y1 or uy > y2 or uz < z1 or uz > z2:
          p2 += 1
          break
        for dx, dy, dz in DIRS:
          p = ux+dx, uy+dy, uz+dz
          if p in vis:
            continue
          vis.add(p)
          if p not in C:
            Q.append(p)
  print(p1)
  print(p2)
