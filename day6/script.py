
with open('day6/in.txt') as f:
	line = [c for c in f.readline().strip()]

	for i in [4, 14]:
		W = line[0:i]
		while i < len(line):
			if len(set(W)) == len(W):
				print(i)
				break
			W = W[1:] + [line[i]]
			i += 1
