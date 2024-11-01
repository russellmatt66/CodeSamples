"""
Efficient solution
"""
def longestSquareStreak(self, nums: list[int]) -> int:
    longest_length = -1
    num_set = set(nums) # O(1) lookup is the key here

    for num in nums:
        current_length = 0
        while num in num_set:
            current_length += 1
            num = num ** 2
        if (current_length >= 2):
            longest_length = max(longest_length, current_length)
            
    return longest_length  