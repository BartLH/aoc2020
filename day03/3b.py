with open('input.txt') as f:
	data = f.read().splitlines()  # doesn't include newlines
# 	data = (
# """..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#""").split('\n')

width = len(data[0])
height = len(data)


def count_trees(xstep, ystep):
	empty = 0
	trees = 0
	x = 0
	for line in data[::ystep]:
		if line[x] == '#':
			trees += 1
		elif line[x] == '.':
			empty += 1
		else:
			raise ValueError
		x = (x + xstep) % width

	print(f"xstep: {xstep}, ystep: {ystep}, trees: {trees}")
	return trees


product = 1
for xstep, ystep in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
	product *= count_trees(xstep, ystep)

print(f"product: {product}")

print("end")  # for debug purposes
