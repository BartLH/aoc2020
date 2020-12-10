with open('input.txt') as f:
	expenses = list(map(int, f.readlines()))

result = 0
for i1, expense1 in enumerate(expenses):
	for i2, expense2 in enumerate(expenses):
		if i1 != i2 and expense1 + expense2 == 2020:
			result = expense1 * expense2
			break
	if result:
		break

if result:
	print("{} * {} = {}".format(expense1, expense2, result))
else:
	print("No result found")
