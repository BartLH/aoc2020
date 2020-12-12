with open('input.txt') as f:
	data = f.read()
# data = """F10
# N3
# F7
# R90
# F11"""


def move_wp(instr, value):
	if instr == 'N':
		waypoint[1] += value
	elif instr == 'S':
		waypoint[1] -= value
	elif instr == 'E':
		waypoint[0] += value
	elif instr == 'W':
		waypoint[0] -= value


pos = [0, 0]
waypoint = [10, 1]
for instr in data.splitlines():
	instr, value = instr[0], int(instr[1:])
	if instr in 'NEWS':
		move_wp(instr, value)
	elif instr == 'L':
		for _ in range(value // 90):
			waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
	elif instr == 'R':
		for _ in range(value // 90):
			waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
	elif instr == 'F':
		pos[0] += value * waypoint[0]
		pos[1] += value * waypoint[1]

print(pos)
print(abs(pos[0]) + abs(pos[1]))
