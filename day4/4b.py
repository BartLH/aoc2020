import re

with open('input.txt') as f:
	data = f.read()
# 	data = (  # invalid passports
# """eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
#
# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946
#
# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
#
# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007"""
# 	)
# 	data = (  # valid passports
# """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f
#
# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
#
# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022
#
# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""
# 	)

mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

data = data.strip().split('\n\n')

valids = 0
for passport in data:
	fields = re.split(r'\s', passport)
	fields = {field.split(':')[0]: field.split(':')[1] for field in fields}
	for key in mandatory_fields:
		if key not in fields.keys():
			break
		value = fields[key]
		if key == 'byr' or key == 'iyr' or key == 'eyr':
			m = re.match(r'^\d{4}$', value)  # '^' is implied by re.match, but I prefer writing it explicitly
			if m:
				year = int(value)
				if key == 'byr' and (year < 1920 or year > 2002):
					break
				elif key == 'iyr' and (year < 2010 or year > 2020):
					break
				elif key == 'eyr' and (year < 2020 or year > 2030):
					break
			else:
				break
		elif key == 'hgt':
			m = re.match(r'^(\d+)(in|cm)$', value)
			if m:
				height = int(m[1])
				unit = m[2]
				if unit == 'cm' and (height < 150 or height > 193):
					break
				elif unit == 'in' and (height < 59 or height > 76):
					break
			else:
				break
		elif key == 'hcl':
			m = re.match(r'^#[0-9a-f]{6}$', value)
			if not m:
				break
		elif key == 'ecl':
			if value not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
				break
		elif key == 'pid':
			m = re.match(r'^\d{9}$', value)
			if not m:
				break
	else:
		valids += 1

print(f"Valid passports: {valids}")

print("end")  # for debug purposes
