import copy
from collections import Counter

with open('input.txt') as f:
	data = f.read()
# data = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL"""
layout = [list(row) for row in data.splitlines()]
width = len(layout[0])
height = len(layout)


def count_seats(layout, row, col):
	c = Counter()

	if row != 0:
		dy = 1
		while row - dy > 0 and layout[row - dy][col] == '.':
			dy += 1
		c.update(layout[row - dy][col])         # top

		if col != 0:
			dx = 1
			dy = 1
			while row - dy > 0 and col - dx > 0 and layout[row - dy][col - dx] == '.':
				dx += 1
				dy += 1
			c.update(layout[row - dy][col - dx])  # top left
		if col != width - 1:
			dx = 1
			dy = 1
			while row - dy > 0 and col + dx < width - 1 and layout[row - dy][col + dx] == '.':
				dx += 1
				dy += 1
			c.update(layout[row - dy][col + dx])  # top right
	if row != height - 1:
		dy = 1
		while row + dy < height - 1 and layout[row + dy][col] == '.':
			dy += 1
		c.update(layout[row + dy][col])  # bottom

		if col != 0:
			dx = 1
			dy = 1
			while row + dy < height - 1 and col - dx > 0 and layout[row + dy][col - dx] == '.':
				dx += 1
				dy += 1
			c.update(layout[row + dy][col - dx])  # bottom left
		if col != width - 1:
			dx = 1
			dy = 1
			while row + dy < height - 1 and col + dx < width - 1 and layout[row + dy][col + dx] == '.':
				dx += 1
				dy += 1
			c.update(layout[row + dy][col + dx])  # bottom right
	if col != 0:
		dx = 1
		while col - dx > 0 and layout[row][col - dx] == '.':
			dx += 1
		c.update(layout[row][col - dx])          # left
	if col != width - 1:
		dx = 1
		while col + dx < width - 1 and layout[row][col + dx] == '.':
			dx += 1
		c.update(layout[row][col + dx])          # right

	return c


def change_seats(layout):
	new_layout = [['' for _ in range(width)] for _ in range(height)]
	changed = False
	for row in range(height):
		for col in range(width):
			c = count_seats(layout, row, col)
			seat = layout[row][col]
			if seat == 'L' and c['#'] == 0:
				new_layout[row][col] = '#'
				changed = True
			elif seat == '#' and c['#'] >= 5:
				new_layout[row][col] = 'L'
				changed = True
			else:
				new_layout[row][col] = layout[row][col]
	return new_layout, changed


changed = True
while changed:
	layout, changed = change_seats(layout)

print(sum(row.count('#') for row in layout))

print("end")
