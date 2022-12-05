import re

with open('day5/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]

	# stacks = [
	# 	"ZN",
	# 	"MCD",
	# 	"P",
	# ]

	stacks = [
		"WMLF",
		"BZVMF",
		"HVRSLQ",
		"FSVQPMTJ",
		"LSW",
		"FVPMRJW",
		"JQCPNRF",
		"VHPSZWRB",
		"BMJCGHZW",
	]
	
	p1 = [list(s) for s in stacks]
	p2 = [list(s) for s in stacks]

	for line in "\n".join(lines).split("\n\n")[1].split("\n"):
		m = re.match("move (\d+) from (\d+) to (\d+)", line)
		amt, src, dst = [int(n) for n in m.groups()]

		for _ in range(0, amt):
			crate = p1[src-1].pop()
			p1[dst-1].append(crate)

		crates = reversed([p2[src-1].pop() for _ in range(0, amt)])
		p2[dst-1].extend(crates)

	print("".join([pile[-1] for pile in p1]))
	print("".join([pile[-1] for pile in p2]))
