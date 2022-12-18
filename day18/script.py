DIRS = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

with open('day18/in.txt') as f:
  lines = [l.strip() for l in f.readlines()]
  
  C = set()
  for line in lines:
    p = tuple([int(c) for c in line.split(',')])
    C.add(p)

  x1 = min([c[0] for c in C])-1
  x2 = max([c[0] for c in C])+1
  y1 = min([c[1] for c in C])-1
  y2 = max([c[1] for c in C])+1
  z1 = min([c[2] for c in C])-1
  z2 = max([c[2] for c in C])+1

  outside = set()
  Q = [(x1, y1, z1)]
  V = set(Q)
  while Q:
    ux, uy, uz = Q.pop(0)
    if x1 <= ux <= x2 and y1 <= uy <= y2 and z1 <= uz <= z2:
      outside.add((ux, uy, uz))
      for dx, dy, dz in DIRS:
        p = ux+dx, uy+dy, uz+dz
        if p not in V and p not in C:
          V.add(p)
          Q.append(p)

  p1 = 0
  p2 = 0
  for x, y, z in C:
    for dx, dy, dz in DIRS:
      n = (x+dx, y+dy, z+dz)
      if n in C:
        continue
      p1 += 1
      if n in outside:
        p2 += 1
      
  print(p1)
  print(p2)
