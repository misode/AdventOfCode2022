with open('day20/in.txt') as f:
  lines = [l.strip() for l in f.readlines()]

  N = len(lines)
  for (rounds, multiplier) in [(1, 1), (10, 811589153)]:
    nums = [(i, multiplier*int(l)) for i, l in enumerate(lines)]
    for r in range(rounds):
      for c in range(N):
        i = next(j for j, n in enumerate(nums) if n[0] == c)
        n = nums[i]
        nums.remove(n)
        j = (i + n[1]) % (N-1)
        nums.insert(j, n)
    zero = next(i for i, n in enumerate(nums) if n[1] == 0)
    print(sum([nums[(zero + i) % N][1] for i in (1000, 2000, 3000)]))
