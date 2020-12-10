with open('input.txt') as f:
	data = f.read()
# data  = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6"""

instructions = [instr.split(' ') for instr in data.splitlines()]
acc = 0
ptr = 0
running = True

visited_ptrs = []
while True:
	if ptr in visited_ptrs or ptr > len(instructions):
		break
	op, arg = instructions[ptr]
	arg = int(arg)
	visited_ptrs.append(ptr)
	if op == 'acc':
		acc += arg
		ptr += 1
	elif op == 'jmp':
		ptr += arg
	elif op == 'nop':
		ptr += 1
	else:
		raise ValueError

print(f"acc: {acc}")

print("end")
