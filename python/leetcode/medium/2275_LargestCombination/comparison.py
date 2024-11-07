import numpy as np
import matplotlib.pyplot as plt

import time
import random
import sys

from efficient import createCandidates
from efficient import Solution
from bruteforce import SolutionBF

num_iter = int(sys.argv[1])
N_max = int(sys.argv[2])

N = np.linspace(1,N_max, num=N_max, dtype=int) # list_lengths
# print(N)

eff_times = []
bf_times = []

int_min = 1
int_max = 1e7

solEff = Solution()
solBF = SolutionBF()
for n in N:
    count = 0
    eff_time_count = 0 # running tally
    bf_time_count = 0 # running tally

    while (count < num_iter):
        candidates = createCandidates(n, int_min, int_max)
        
        start_time_eff = time.time()
        maxlength_eff = solEff.largestCombination(candidates)
        stop_time_eff = time.time()
        eff_time_count += (stop_time_eff - start_time_eff)

        start_time_bf = time.time()
        maxlength_bf = solBF.largestCombinationBF(candidates)
        stop_time_bf = time.time()
        bf_time_count += (stop_time_bf - start_time_bf)
        count += 1
    
    eff_time_count /= float(num_iter) # average over a number of iterations is better measure
    bf_time_count /= float(num_iter)

    eff_times.append(eff_time_count * 1e3) # convert time to ms for visualization
    bf_times.append(bf_time_count * 1e3)

print(eff_times)
print(bf_times)

plt.title('Runtime of Efficient vs. Brute-Force solution for LC2275 with num_iter = {}'.format(num_iter))
plt.ylabel('Time (ms)')
plt.xlabel('N')
plt.xlim(N[0], N[-1])
plt.xticks(N)

a = (eff_times[-1] - eff_times[0]) / len(eff_times)
b = eff_times[-1] - a * N[-1]
plt.semilogy(N, eff_times, color='blue', label='Efficient')
plt.semilogy(N, a * N + b, linestyle='dashed', color='orange', label='O(N)')

k = 2**(np.log2(bf_times[-1]) - N[-1])
# k = bf_times[-1] / (2**N - 1)
plt.semilogy(N, bf_times, color='green', label='Brute-Force')
plt.semilogy(N, k * 2**N, linestyle='dashed', color='red', label='O($2^N$)')

plt.legend()
plt.show()