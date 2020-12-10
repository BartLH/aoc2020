import re

with open('input.txt') as f:
	data = f.read()
# 	data = (
# """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm
#
# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929
#
# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm
#
# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in"""
# 	)

mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

data = data.split('\n\n')

valids = 0
for passport in data:
	fields = re.split(r'\s', passport)
	for mandatory_key in mandatory_fields:
		present = False
		for field in fields:
			key = field.split(':')[0]
			if key == mandatory_key:
				present = True
				break
		if not present:
			break
	else:
		valids += 1

print(f"Valid passports: {valids}")

print("end")  # for debug purposes
