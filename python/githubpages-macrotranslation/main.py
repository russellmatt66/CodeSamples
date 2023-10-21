with open('input.txt', 'r') as inputfile:
		oldconfig = inputfile.read()

macros = oldconfig.split('],')

with open('newmacros.txt', 'w') as outputfile:
		for macro in macros:
				outputfile.write('    '+macro+'],\n')
