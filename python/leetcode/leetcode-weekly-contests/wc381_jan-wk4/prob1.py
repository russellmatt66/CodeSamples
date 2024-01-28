# https://leetcode.com/contest/weekly-contest-381/problems/minimum-number-of-pushes-to-type-word-i/
class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0
        num_push = 0
        for c in range(len(word)):
            # print(c)
            if c % 8 == 0:
                num_push += 1
            pushes += num_push
        return pushes
