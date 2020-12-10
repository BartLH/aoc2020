with open('input.txt') as f:
	data = f.read()
# data = """abc
#
# a
# b
# c
#
# ab
# ac
#
# a
# a
# a
# a
#
# b"""

data = data.split('\n\n')

total = 0
for group in data:
	questions = [set(person) for person in group.splitlines()]
	intersect = set.intersection(*questions)
	total += len(intersect)

print(f"Sum of counts: {total}")
