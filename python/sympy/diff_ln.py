from sympy import *
import sys

# Takes derivatives of ln[(1 + x) / (1 - x)]

derivative_order = int(sys.argv[1])

x = symbols('x')

init_printing(use_unicode=True)

expr = log((1+x) / (1-x))

for i in range(derivative_order):
	print(simplify(diff(expr, x, i + 1)))
