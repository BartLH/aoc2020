from collections import defaultdict
import re

with open('input.txt') as f:
	data = f.read()
# data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags."""

rules = data.splitlines()

bags = defaultdict(list)
for rule in rules:
	outer, inner = rule.split('contain ')
	outer_colour = outer.split(' bag')[0]
	for m in re.findall(r'(\d*) ([a-z ]+) bag', inner):
		if m[0]:
			bags[m[1]].append(outer_colour)


def count_colours(bag_colour, colours):
	colours.update(bags[bag_colour])
	for bag in bags[bag_colour]:
		if bag:
			count_colours(bag, colours)


colours = set()
count_colours('shiny gold', colours)

print(f"number of colours: {len(colours)}")

print("end")
