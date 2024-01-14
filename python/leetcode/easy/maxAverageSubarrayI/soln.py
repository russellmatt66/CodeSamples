class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        # First window
        for i in range(k):
            sum += nums[i]
        
        max_avg = sum / k # Use first average as a candidate

        # Check all the other windows in one pass
        for j in range(k,len(nums)):
            sum += nums[j] # Most efficient way to create a new window
            sum -= nums[j-k] 
            max_avg = max(max_avg, sum / k)
        
        return max_avg
