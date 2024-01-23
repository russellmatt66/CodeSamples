Small script to fix formatting issue in the MathJax configuration of my Github Pages project.

The issue: All of the MathJax macros were defined in a single line.

The solution: split() the macros up, place one per each line, and then add the characters split() took away back in. 

input.txt - The problematically-formatted macros
newmacros.txt - The macros formatted in an unproblematic manner
newstruct.txt - The unproblematically-formatted macros situated in the necessary MathJax-related syntax
