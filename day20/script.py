from collections import deque
import re

with open('day20/in.txt') as f:
  lines = [l.strip() for l in f.readlines()]

  nums = [(i, int(l)) for i, l in enumerate(lines)]
  N = len(nums)
  mixed = set()
  i = 0
  while len(mixed) < N:
    n = nums[i]
    if n in mixed:
      i = (i + 1) % N
      continue
    nums.remove(n)
    j = (i + n[1]) % (N-1)
    nums.insert(j, n)
    mixed.add(n)

  zero = next((i for i, n in enumerate(nums) if n[1] == 0))
  print(nums[(zero + 1000) % N][1] + nums[(zero + 2000) % N][1] + nums[(zero + 3000) % N][1])
