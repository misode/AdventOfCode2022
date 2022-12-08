
with open('day8/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]

	G = [[int(c) for c in line] for line in lines]
	n = len(lines)
	assert(n == len(lines[0]))

	total_vis = 0
	for i in range(0, n):
		for j in range(0, n):
			this = G[i][j]
			for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
				vis = True
				for k in range(1, n):
					ii = i + k*dir[0]
					jj = j + k*dir[1]
					if ii < 0 or ii >= n or jj < 0 or jj >= n:
						break
					if G[ii][jj] >= this:
						vis = False
						break
				if vis:
					total_vis += 1
					break
	print(total_vis)

	max_score = 0
	for i in range(0, n):
		for j in range(0, n):
			this = G[i][j]
			score = 1
			for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
				c = 0
				for k in range(1, n):
					ii = i + k*dir[0]
					jj = j + k*dir[1]
					if ii < 0 or ii >= n or jj < 0 or jj >= n:
						break
					if G[ii][jj] >= this:
						c += 1
						break
					c += 1
				score *= c
			max_score = max(max_score, score)
	print(max_score)
