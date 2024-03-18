import sys

codefile = sys.argv[1]

print(codefile)

fixed_line = ''
fixed_lines = []
with open(codefile, 'r') as f:
    for line in f:
        fixed_line = line.replace('(', '[')
        fixed_line = fixed_line.replace(')', ']')
        fixed_lines.append(fixed_line)

with open('mm_win_prob_fixed.py', 'w') as f:
    for line in fixed_lines:
        f.write(line)
