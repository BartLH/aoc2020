with open('input.txt') as f:
	data = f.read()
# data = """F10
# N3
# F7
# R90
# F11"""


def move(instr, value):
	if instr == 'N':
		pos[0] += value
	elif instr == 'S':
		pos[0] -= value
	elif instr == 'E':
		pos[1] += value
	elif instr == 'W':
		pos[1] -= value


pos = [0, 0]
dir = 1  # 0: N, 1: E, 2: S, 3: W; start facing east
for instr in data.splitlines():
	instr, value = instr[0], int(instr[1:])
	if instr in 'NEWS':
		move(instr, value)
	elif instr == 'L':
		dir = int(dir - value / 90) % 4
	elif instr == 'R':
		dir = int(dir + value / 90) % 4
	elif instr == 'F':
		move('NESW'[dir], value)

print(pos)
print(abs(pos[0]) + abs(pos[1]))
