from functools import lru_cache

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
end = data[-1] + 3


@lru_cache
def find_path(value):
	if value + 3 == end:
		return 1
	count = 0
	for d in (1, 2, 3):
		if value + d in data:
			count += find_path(value + d)
	return count


total = find_path(0)

print(f"{total} paths")

print("end")
