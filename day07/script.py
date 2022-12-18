from collections import defaultdict

with open('day07/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]
	path = []
	used_size = 0
	sizes = defaultdict(int)

	for line in lines:
		if line.startswith('$'):
			if line.startswith('$ cd /'):
				path = []
			elif line.startswith('$ cd ..'):
				path.pop()
			elif line.startswith('$ cd'):
				path.append(line.removeprefix('$ cd '))
		elif not line.startswith('dir'):
			size = int(line.split(' ')[0])
			used_size += size
			for i in range(0, len(path)):
				key = ".".join(path[0:i+1])
				sizes[key] += size

	print(sum(s for s in sizes.values() if s <= 100000))

	for s in sorted(sizes.values()):
		if 70000000 - used_size + s >= 30000000:
			print(s)
			break
