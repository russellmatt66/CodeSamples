# https://leetcode.com/contest/weekly-contest-422/problems/find-minimum-time-to-reach-last-room-i/

import heapq

# BFS w/out priority queue - exceeds recursion depth
# class Solution:
#     def minTimeToReach(self, moveTime: list[list[int]]) -> int:
#         num_rows = len(moveTime)
#         num_cols = len(moveTime[0])
#         return Solution.bfs(0, 0, 0, num_rows, num_cols, moveTime)

#     # time from (i, j) to the end
#     def bfs(t: int, i: int, j: int, num_rows: int, num_cols: int, moveTime: list[list[int]]) -> int: 
#         if i < 0 or i >= num_rows or j < 0 or j >= num_cols:
#             return float('inf')
            
#         if i == num_rows - 1 and j == num_cols - 1: # the end
#             return t

#         t_l = 1 + max(t, moveTime[i - 1][j]) if i - 1 < 0 else float('inf')
#         t_r = 1 + max(t, moveTime[i + 1][j]) if i + 1 < num_rows else float('inf')
#         t_d = 1 + max(t, moveTime[i][j + 1]) if j + 1 < num_cols else float('inf')
#         t_u = 1 + max(t, moveTime[i][j - 1]) if j - 1 > 0 else float('inf')

#         t_left = Solution.bfs(t_l, i - 1, j, num_rows, num_cols, moveTime)
#         t_right = Solution.bfs(t_r, i + 1, j, num_rows, num_cols, moveTime)
#         t_down = Solution.bfs(t_d, i, j + 1, num_rows, num_cols, moveTime)
#         t_up = Solution.bfs(t_u, i, j - 1, num_rows, num_cols, moveTime)
        
        # return min(t_left, t_right, t_down, t_up)

# BFS w/priority queue
class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        num_rows = len(moveTime)
        num_cols = len(moveTime[0])
        
        # Priority queue to store (time, row, col) with minimum time at the top
        pq = [(0, 0, 0)]  # Start from (0, 0) at time t = 0
        min_time = [[float('inf')] * num_cols for _ in range(num_rows)]
        min_time[0][0] = 0

        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while pq:
            t, i, j = heapq.heappop(pq)

            # If we reached the bottom-right corner, return the time
            if i == num_rows - 1 and j == num_cols - 1:
                return t

            # Explore all possible directions
            for di, dj in directions:
                ni, nj = i + di, j + dj

                # Check if (ni, nj) is within bounds
                if 0 <= ni < num_rows and 0 <= nj < num_cols:
                    # Calculate the earliest time we can enter the next room
                    arrival_time = 1 + max(t, moveTime[ni][nj])

                    # If we find a shorter time for (ni, nj), update and push to the queue
                    if arrival_time < min_time[ni][nj]:
                        min_time[ni][nj] = arrival_time
                        heapq.heappush(pq, (arrival_time, ni, nj))

        return -1  # If we somehow cannot reach (n-1, m-1)

"""
Testcases not passed
"""

"""
Works for all these
"""
moveTime = [
    [94,79,62,27,69,84],
    [6,32,11,82,42,30]
]

# moveTime = [
#     [0, 4],
#     [4, 4]
# ]

# moveTime = [
#     [0, 0, 0],
#     [0, 0, 0]
# ]

# moveTime = [
#     [0, 1],
#     [1, 2]
# ]

sol = Solution()
result = sol.minTimeToReach(moveTime)
print("Minimum time to reach the end:", result)