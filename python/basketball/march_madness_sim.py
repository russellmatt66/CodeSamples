import random
from mm_win_prob_fixed import win_probabilities

picking = True
eps = 1.0e-4

random.seed()

rand_val = 0

while picking:
	print("Please input the matchup seeds:")
	i = int(input())
	j = int(input())
	print(f"The matchup is a {i}-seed versus a {j}-seed")
	print(f"Historically, the chance that {i}-seed beats a {j}-seed is {win_probabilities[i-1,j-1]}")
	print(f"Historically, the chance that {j}-seed beats a {i}-seed is {win_probabilities[j-1,i-1]}")
	if ((win_probabilities[i-1,j-1] + win_probabilities[j-1,i-1]) < (1.0 - eps)):
		print("Looks like this matchup has never occurred before!")
	prob_i_beats_j = int(1000.0 * win_probabilities[i-1,j-1]) 
	rand_val = random.randint(0,999)
	print(f"Random value of {rand_val}")
	print(f"Scaled value of {prob_i_beats_j}") 
	if (rand_val <= prob_i_beats_j):
		print(f"The {i}-seed wins")
	else:
		print(f"The {j}-seed wins")
	print("Still picking? (True or False)")
	picking = eval(input())
