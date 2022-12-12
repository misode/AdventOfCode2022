from collections import deque

with open('day12/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]

	start = (0, 0)
	end = (0, 0)

	G = []
	for r, line in enumerate(lines):
		row = []
		for c, char in enumerate(line):
			if char == 'S':
				start = (r, c)
				char = 'a'
			elif char == 'E':
				end = (r, c)
				char = 'z'
			e = ord(char) - ord('a')
			row.append(e)
		G.append(row)
	R = len(G)
	C = len(G[0])

	visited = set([start])
	queue = deque([(*start, 0)])
	found = False
	while queue and not found:
		r, c, d = queue.popleft()
		if end == (r, c):
			print(d)
			found = True
			break
		for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			r2, c2 = r+dir[0], c+dir[1]
			if r2 < 0 or r2 >= R or c2 < 0 or c2 >= C:
				continue
			if G[r2][c2] <= G[r][c] + 1:
				if (r2, c2) not in visited:
					visited.add((r2, c2))
					queue.append((r2, c2, d+1))

	visited = set([end])
	queue = deque([(*end, 0)])
	found = False
	while queue and not found:
		r, c, d = queue.popleft()
		if G[r][c] == 0:
			print(d)
			found = True
			break
		for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			r2, c2 = r+dir[0], c+dir[1]
			if r2 < 0 or r2 >= R or c2 < 0 or c2 >= C:
				continue
			if G[r2][c2] >= G[r][c] - 1:
				if (r2, c2) not in visited:
					visited.add((r2, c2))
					queue.append((r2, c2, d+1))
