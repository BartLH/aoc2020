with open('input.txt') as f:
	data = f.read().splitlines()
	# data = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

highest_id = 0
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
	if seat_id > highest_id:
		highest_id = seat_id
	# print(f"row: {row}, col: {col}, seat ID: {seat_id}")

print(f"Highest seat ID: {highest_id}")
