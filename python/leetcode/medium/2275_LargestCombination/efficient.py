import sys
import random
import time

# Efficient solution
# O(N)
# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
class Solution:
    def largestCombination(self, candidates: list[int]) -> int: # Find the max number of sets bits at a given position
        numBits = 32
        max_length = 0

        for i in range(numBits):
            count = 0
            for candidate in candidates:
                if (candidate >> i) & 1: # count how many set bits there are at this position
                    count += 1
            if count > max_length:
                max_length = count
        
        return max_length
    

def createCandidates(length: int, int_min: int, int_max: int) -> list[int]:
    candidates = []
    for i in range(length):
        randval = random.randint(int_min, int_max) 
        candidates.append(randval)
    return candidates

def main(candidates: list[int]) -> int:
    sol = Solution()
    max_length = sol.largestCombination(candidates)
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