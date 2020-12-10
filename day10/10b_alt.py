from collections import Counter

with open('input.txt') as f:
	data = f.read()
# data = """16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4"""
# data = """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3"""
data = list(map(int, data.splitlines()))
data.sort()
data.append(data[-1] + 3)

c = Counter()
c[0] = 1
for value in data:
	c[value] = c[value - 1] + c[value - 2] + c[value - 3]

print(f"{c[data[-1]]} paths")

print("end")
