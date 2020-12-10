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

empty = 0
trees = 0
x = 0
for line in data:
	if line[x] == '#':
		trees += 1
	elif line[x] == '.':
		empty += 1
	else:
		raise ValueError
	x = (x + 3) % width

print("{} lines: {} trees, {} empty".format(height, trees, empty))

print("end")  # for debug purposes
