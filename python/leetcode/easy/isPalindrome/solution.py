class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = True
        i, j = 0, len(s) - 1
        while s[i] == s[j] and i < j:
            i += 1
            j -= 1

        if i < j:
            res = False

        return res
    
if __name__ == "__main__":
    sol = Solution()
    s = "ababab"
    is_pal = sol.isPalindrome(s)
    print(is_pal)