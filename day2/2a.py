with open('input.txt') as f:
	data = f.readlines()

valid_passwords = []
for line in data:
	policy, password = line.split(': ')
	letter = policy[-1]
	lower, upper = map(int, policy[0:-2].split('-'))
	n = password.count(letter)
	if lower <= n <= upper:
		valid_passwords.append(password)

print(len(valid_passwords))

print("end")  # for debug purposes
