# I think this whole approach is flawed, because I based what the NEW should be on Chat-GPT's hallucination. Stick with the OLD, and just write a script that separates the macros with newlines.
def parse_macros(macro):
	# NEW= name: ["definition", numargs]\n
	# OLD= name:["Macro","definition", numargs],
	# macro= name:["Macro","definition",numargs
	namepos = macro.find(':[')
	name = macro[:namepos]
	# This bit below isn't working, CHAT-GPT says to use regex
	defpos = macro.rfind('\"Macro\",')
	numargs = macro[len(macro)-1]
	definition = macro[defpos+len('\"Macro\",'):len(macro)-2]
	return name, definition, numargs

with open('input.txt', 'r') as inputfile:
	oldconfig = inputfile.read() # one big string

macros = oldconfig.split('],') # list of strings

with open("newmacros.txt", "a") as outputfile:	
	for macro in macros:
		name, definition, numargs = parse_macros(macro)
		outputfile.write(f"{name}: [{definition}, {numargs}]\n")
		

