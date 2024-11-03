# O(N^2) time
# O(N) space
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        res = True
        if len(s) != len(goal):
            return False

        clength = 0
        while s != goal and clength < len(s):
            lmost_char = s[0]
            new_s = []
            for i in range(1,len(s)):
                new_s.append(s[i])
            new_s.append(lmost_char)
            s = "".join(new_s)
            clength += 1
        
        if clength == len(s): res = False

        return res