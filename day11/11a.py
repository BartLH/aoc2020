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
		c.update(layout[row - 1][col])          # top
		if col != 0:
			c.update(layout[row - 1][col - 1])  # top left
		if col != width - 1:
			c.update(layout[row - 1][col + 1])  # top right
	if row != height - 1:
		c.update(layout[row + 1][col])          # bottom
		if col != 0:
			c.update(layout[row + 1][col - 1])  # bottom left
		if col != width - 1:
			c.update(layout[row + 1][col + 1])  # bottom right
	if col != 0:
		c.update(layout[row][col - 1])          # left
	if col != width - 1:
		c.update(layout[row][col + 1])          # right

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
			elif seat == '#' and c['#'] >= 4:
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
