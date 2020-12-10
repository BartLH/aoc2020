with open('input.txt') as f:
	expenses = list(map(int, f.readlines()))

result = 0
for i1, expense1 in enumerate(expenses):
	for i2, expense2 in enumerate(expenses):
		for i3, expense3 in enumerate(expenses):
			if i1 != i2 and i2 != i3 and expense1 + expense2 + expense3 == 2020:
				result = expense1 * expense2 * expense3
				break
		if result:
			break
	if result:
		break

if result:
	print("{} * {} * {} = {}".format(expense1, expense2, expense3, result))
else:
	print("No result found")
