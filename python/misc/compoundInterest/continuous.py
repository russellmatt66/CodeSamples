import numpy as np
import matplotlib.pyplot as plt
import sys

yar = float(sys.argv[1])
gamma = yar / 365 # approximation of continuous R.O.R

num_years = int(sys.argv[2])
t = np.linspace(0, 365 * num_years, num=365*num_years)

base = float(sys.argv[3])
principal = base * np.exp(gamma * t)

discrete = []
discrete.append(base)
dgamma = yar / 26 # invest every two weeks 
investment_addition = float(sys.argv[4])
t_2weeks = np.linspace(0, 14*26*num_years, num=26*num_years)

money_invested = []
money_invested.append(base)

for i in range(1, num_years * 26):
	discrete.append(discrete[i-1] * (1.0 + dgamma) + investment_addition)  
	money_invested.append(investment_addition)

plt.semilogy(t, principal, t_2weeks, np.asarray(discrete), t_2weeks, np.asarray(money_invested))

plt.show()
