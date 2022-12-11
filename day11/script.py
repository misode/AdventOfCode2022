from collections import defaultdict
from dataclasses import dataclass

def product(lst):
  p = 1
  for i in lst:
    p *= i
  return p

@dataclass
class Monkey:
	items: list[int]
	op: tuple
	test: int
	if_true: int
	if_false: int
	inspections = 0

	def __init__(self, lines: list[str]):
		self.items = [int(n) for n in lines[1].removeprefix('Starting items: ').split(', ')]
		self.op = tuple([n if n in ['old', '*', '+'] else int(n) for n in lines[2].removeprefix('Operation: new = ').split(' ')])
		self.test = int(lines[3].removeprefix('Test: divisible by '))
		self.if_true = int(lines[4].removeprefix('If true: throw to monkey '))
		self.if_false = int(lines[5].removeprefix('If false: throw to monkey '))

with open('day11/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]

	for rounds, relief in [(20, True), (10000, False)]:
		monkeys = [Monkey(l.split('\n')) for l in '\n'.join(lines).split('\n\n')]
		combined_mod = product([m.test for m in monkeys])

		for r in range(rounds):
			for i, monkey in enumerate(monkeys):
				a, op, b = monkey.op
				for item in monkey.items:
					monkey.inspections += 1
					item_a: int = item if a == 'old' else a
					item_b: int = item if b == 'old' else b
					item = item_a * item_b if op == '*' else item_a + item_b
					if relief:
						item = item // 3
					else:
						item = item % combined_mod
					result = (item % monkey.test) == 0
					throw = monkey.if_true if result else monkey.if_false
					monkeys[throw].items.append(item)
				monkey.items.clear()
		print(product(sorted([m.inspections for m in monkeys])[-2:]))
