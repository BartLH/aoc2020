with open('input.txt') as f:
	expenses = list(map(int, f.readlines()))
	# expenses = [1721, 979, 366, 299, 675, 1456]

max_level = 3
ref_value = 2020


def compute(subtotal, level, used_indices, expenses, values):
	for i, expense in enumerate(expenses):
		if i not in used_indices:
			if level == max_level:
				if subtotal + expense == ref_value:
					values.append(expense)
					return True
			else:
				if compute(subtotal + expense, level + 1, used_indices + [i], expenses, values):
					values.append(expense)
					return True


values = []
compute(0, 1, [], expenses, values)
product = 1
for value in values:
	product *= value

print(values)
print(product)
