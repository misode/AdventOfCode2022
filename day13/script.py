from collections import deque
import json
from functools import cmp_to_key

with open('day13/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]

	groups = [tuple([json.loads(l) for l in g.split("\n")]) for g in "\n".join(lines).split("\n\n")]

	def cmp(a, b):
		if type(a) == int and type(b) == int:
			return a - b
		if type(a) == int:
			return cmp([a], b)
		if type(b) == int:
			return cmp(a, [b])
		for i in range(max([len(a), len(b)])):
			if i >= len(a):
				return -1
			if i >= len(b):
				return 1
			x = cmp(a[i], b[i])
			if x != 0:
				return x
		return 0

	p0 = 0
	for i, pair in enumerate(groups):
		x = cmp(pair[0], pair[1])
		assert x != 0
		if x < 0:
			p0 += (i+1)
	print(p0)

	packets = [json.loads(l) for l in lines if l]
	packets.append([[2]])
	packets.append([[6]])

	packets = sorted(packets, key=cmp_to_key(cmp))
	a = packets.index([[2]]) + 1
	b = packets.index([[6]]) + 1
	print(a * b)
	
