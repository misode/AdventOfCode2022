"""
A = rock
B = paper
C = scissors

X = rock
Y = paper
Z = scissors
"""

MAP = {
	"X": "A",
	"Y": "B",
	"Z": "C",
}

MAP2 = {
	"XA": "C",
	"XB": "A",
	"XC": "B",
	"YA": "A",
	"YB": "B",
	"YC": "C",
	"ZA": "B",
	"ZB": "C",
	"ZC": "A",
}

SCORE = {
	"A": 1,
	"B": 2,
	"C": 3,
}

with open('day02/in.txt') as f:
	lines = [l.strip() for l in f.readlines()]

	score = 0
	for line in lines:
		[theirs, B] = line.split(' ')
		ours = MAP[B]
		if theirs == ours:
			score += 3
		elif (theirs == "A" and ours == "B") or (theirs == "B" and ours == "C") or (theirs == "C" and ours == "A"):
			score += 6
		score += SCORE[ours]
	print(score)


	score = 0
	for line in lines:
		[theirs, B] = line.split(' ')
		ours = MAP2[B+theirs]
		if theirs == ours:
			score += 3
		elif (theirs == "A" and ours == "B") or (theirs == "B" and ours == "C") or (theirs == "C" and ours == "A"):
			score += 6
		score += SCORE[ours]
	print(score)
