# https://leetcode.com/contest/weekly-contest-422/problems/find-minimum-time-to-reach-last-room-ii/description/

import heapq

class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        num_rows = len(moveTime)
        num_cols = len(moveTime[0])
        
        # Priority queue to store (time, row, col, num_move) with minimum time at the top
        pq = [(0, 0, 0, 1)]  # Start from (0, 0) at time t = 0
        min_time = [[float('inf')] * num_cols for _ in range(num_rows)]
        min_time[0][0] = 0

        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while pq:
            t, i, j, num_move = heapq.heappop(pq)

            # If we reached the bottom-right corner, return the time
            if i == num_rows - 1 and j == num_cols - 1:
                return t

            # Explore all possible directions
            for di, dj in directions:
                ni, nj = i + di, j + dj

                # Check if (ni, nj) is within bounds
                if 0 <= ni < num_rows and 0 <= nj < num_cols:
                    # Calculate the earliest time we can enter the next room
                    if num_move % 2:
                        arrival_time = 1 + max(t, moveTime[ni][nj])
                    else: 
                        arrival_time = 2 + max(t, moveTime[ni][nj])
                    
                    # If we find a shorter time for (ni, nj), update and push to the queue
                    if arrival_time < min_time[ni][nj]:
                        min_time[ni][nj] = arrival_time
                        heapq.heappush(pq, (arrival_time, ni, nj, num_move + 1))

        return -1  # If we somehow cannot reach (n-1, m-1)