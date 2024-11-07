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