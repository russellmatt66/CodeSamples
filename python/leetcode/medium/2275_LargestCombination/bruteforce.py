import sys
import random
import time

from itertools import combinations

# Brute-force solution
# O(2^N)
# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
class SolutionBF:
    def largestCombinationBF(self, candidates: list[int]) -> int:
        max_length = 0

        comb_dict = {}
        idx = 0
        for r in range(1, len(candidates) + 1):
            for perm in set(combinations(candidates, r)): # for uniqueness
                comb_dict[idx] = list(perm)
                idx += 1
        
        # print(comb_dict)
        n = 32
        for idx, combination in comb_dict.items():
            bitwise_and = int('1' * n, 2) # all 1's
            for integer in combination: 
                bitwise_and &= integer
            if bitwise_and > 0:
                if len(combination) > max_length:
                    max_length = len(combination)

        return max_length
    

def createCandidates(length: int, int_min: int, int_max: int) -> list[int]:
    candidates = []
    for i in range(length):
        randval = random.randint(int_min, int_max) 
        candidates.append(randval)
    return candidates

def main(candidates: list[int]) -> int:
    sol = SolutionBF()
    max_length = sol.largestCombinationBF(candidates)
    return max_length

if __name__ == "__main__":
    num_iter = int(sys.argv[1])
    list_length = int(sys.argv[2])

    int_min = 1
    int_max = 1e7
    
    start_time = time.time()
    count = 0
    while (count < num_iter):
        candidates = createCandidates(list_length, int_min, int_max)
        max_length = main(candidates)
        count += 1
    stop_time = time.time()

    avg_time = (stop_time - start_time) / float(num_iter)
    print("Avg time per iterations for {} iterations, with list length {}, is {} seconds".format(num_iter, list_length, avg_time))
