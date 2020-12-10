import copy

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


def run_program(instructions):
	acc = 0
	ptr = 0

	visited_ptrs = []
	while True:
		if ptr in visited_ptrs or ptr < 0:
			return None
		if ptr > len(instructions) - 1:
			return acc
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


for i, (op, arg) in enumerate(instructions):
	if op == 'nop' and arg != '+0':
		instr_copy = copy.deepcopy(instructions)
		instr_copy[i][0] = 'jmp'
	elif op == 'jmp':
		instr_copy = copy.deepcopy(instructions)
		instr_copy[i][0] = 'nop'
	else:
		continue
	result = run_program(instr_copy)
	if result is not None:
		print(f"acc: {result}")
		break

print("end")
