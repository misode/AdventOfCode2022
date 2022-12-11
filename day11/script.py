from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Monkey:
	items: list[int]
	op: tuple[str | int, str, str | int]
	test: int
	if_true: int
	if_false: int

def parse_monkey(lines: list[str]):
	return Monkey(
		items=[int(n) for n in lines[1].removeprefix('Starting items: ').split(', ')],
		op=tuple([n if n in ['old', '*', '+'] else int(n) for n in lines[2].removeprefix('Operation: new = ').split(' ')]),
		test=int(lines[3].removeprefix('Test: divisible by ')),
		if_true=int(lines[4].removeprefix('If true: throw to monkey ')),
		if_false=int(lines[5].removeprefix('If false: throw to monkey ')),
	)

with open('day11/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]
	
	monkeys = [
		parse_monkey(l.split('\n'))
		for l in '\n'.join(lines).split('\n\n')
	]
	inspected = defaultdict(int)

	for _ in range(20):
		for i, monkey in enumerate(monkeys):
			a, op, b = monkey.op
			for item in monkey.items:
				inspected[i] += 1
				item_a: int = item if a == 'old' else a
				item_b: int = item if b == 'old' else b
				item = item_a * item_b if op == '*' else item_a + item_b
				item = item // 3
				result = (item % monkey.test) == 0
				throw = monkey.if_true if result else monkey.if_false
				monkeys[throw].items.append(item)
			monkey.items.clear()
	A = sorted(inspected.values())
	print(A[-1] * A[-2])
