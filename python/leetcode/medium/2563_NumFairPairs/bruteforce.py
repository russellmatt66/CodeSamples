# Brute Force
class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if ((nums[i] + nums[j]) >= lower and (nums[i] + nums[j]) <= upper):
                    count += 1
        return count