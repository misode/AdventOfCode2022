from collections import defaultdict

with open('day7/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]

	path = []
	used_size = 0
	sizes = defaultdict(int)

	for line in lines:
		if line.startswith('$'):
			if line.startswith('$ cd'):
				if line.startswith('$ cd /'):
					path = []
				elif line.startswith('$ cd ..'):
					path.pop()
				else:
					path.append(line.removeprefix('$ cd '))
				pass
			elif line.startswith('$ ls'):
				pass
			else:
				raise ValueError()
		else:
			if line.startswith('dir'):
				pass
			else:
				size = int(line.split(' ')[0])
				used_size += size
				for i in range(0, len(path)):
					key = ".".join(path[0:i+1])
					sizes[key] += size

	p1 = 0
	for path in sizes:
		if sizes[path] <= 100000:
			p1 += sizes[path]
	print(p1)

	unused_size = 70000000 - used_size

	A = sorted([sizes[path] for path in sizes])
	for a in A:
		if a >= 30000000 - unused_size:
			print(a)
			break
