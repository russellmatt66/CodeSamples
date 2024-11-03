# O(N^2) time
# O(N) space
class Solution:
  def rotateString(self, s: str, goal: str) -> bool:
    return len(s) == len(goal) and goal in s + s