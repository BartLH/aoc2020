import itertools

with open('input.txt') as f:
	data = f.read()
pre_len = 25
# data = """35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576"""
# pre_len = 5

data = list(map(int, data.splitlines()))

for i, number in enumerate(data[pre_len:]):
	i += pre_len
	sums = [a + b for a, b in itertools.combinations(data[i - pre_len:i], 2)]
	if number not in sums:
		print(number)
		break
else:
	print("All numbers valid")
