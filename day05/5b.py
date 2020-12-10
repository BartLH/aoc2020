with open('input.txt') as f:
	data = f.read().splitlines()
# data = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

all_ids = []
for seat in data:
	row_data = seat[0:7]
	col_data = seat[7:]
	row = 0
	for i, half in enumerate(row_data):
		if half == 'B':
			row += 1 << (6 - i)
	col = 0
	for i, half in enumerate(col_data):
		if half == 'R':
			col += 1 << (2 - i)

	seat_id = row * 8 + col
	all_ids.append(seat_id)

all_ids.sort()
for i, id in enumerate(all_ids[:-1]):
	res = all_ids[i + 1] - id - 1
	if res:
		print(f"i: {i}, id: {id}, next id: {all_ids[i + 1]}")
		print(f"Your ID: {id + 1}")
