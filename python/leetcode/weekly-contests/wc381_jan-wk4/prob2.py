# https://leetcode.com/contest/weekly-contest-381/problems/count-the-number-of-houses-at-a-certain-distance-i/
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        def countMinDistance(pair: (int, int), x, y):
            i, j = min(pair), max(pair)
            if ((i == x and j == y) or (i == y and j == x)):
                return 1
            if ((i <= x and j >= x) and (i <= y and j >= y)): # Case I and II - x,y b/w i,j
                return abs(i-j) - abs(x-y)
            if (x <= i and (i<=y and y <=j)): # Case III - x to the left of i, y b/w i,j
                return min(abs(i-j), abs(i-x) + abs(j-y))
            if (x <= i and y >= j): # Case IV - x to the left of i, y to the right of j
                return min(abs(i-j), abs(i-x) + abs(j-y))
            if (y <= i and (i <= x and x<= j)): # Case V - y to the left of i, x in b/w i,j
                return min(abs(i-j), abs(i-y) + abs(j-x))
            if (y <= i and x >= j): # Case VI - y to the left of i, x to the right of j
                return min(abs(i,j), abs(i-y) + abs(j-x))
            if ((i <= y and j >= y) and x >= j): # Case VII - 
                return min(abs(i,j), abs(i-y) + abs(j-x))
            return -1
        
        results = [0] * n

        
        houses = []
        for i in range(1,n+1):
            for j in range(1,n+1):
                if (i != j):
                    houses.append((i,j))
        
        # print(houses)
        temp = 0
        for pair in houses:
            temp = countMinDistance(pair, x, y)
            print(pair, temp)
            results[temp - 1] += 1
            
        # print(results)
        return results
