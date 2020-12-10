with open('input.txt') as f:
	data = f.read()
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
data = [0] + list(map(int, data.splitlines()))
data.sort()
data.append(data[-1] + 3)

diffs = [data[i + 1] - v for i, v in enumerate(data[:-1])]

print(f"count(1) = {diffs.count(1)}, count(3) = {diffs.count(3)}, count(1) * count(3) = {diffs.count(1) * diffs.count(3)}")

print("end")
