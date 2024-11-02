class Solution:
    def makeFancyString(self, s: str) -> str:
        num_consec = 1
        res = []
        res.append(s[0])
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                num_consec += 1
            else:
                num_consec = 1
            if num_consec < 3:
                res.append(s[i])
        return "".join(res) 