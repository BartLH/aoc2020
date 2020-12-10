with open('input.txt') as f:
	data = f.readlines()

valid_passwords = []
for line in data:
	policy, password = line.split(': ')
	letter = policy[-1]
	index1, index2 = map(int, policy[0:-2].split('-'))
	if (password[index1 - 1] == letter) ^ (password[index2 - 1] == letter):
		valid_passwords.append(password)

print(len(valid_passwords))

print("end")  # for debug purposes
