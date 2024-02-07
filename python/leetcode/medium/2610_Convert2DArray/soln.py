# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/submissions/1166482971/
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq_dict = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else: 
                freq_dict[num] += 1
        
        num_rows = max(freq_dict.values())
        print(num_rows)

        matrix = [0] * num_rows
        print(matrix)
        for i in range(num_rows):
            matrix[i] = []
        print(matrix)

        for row in matrix:
            for num, freq in freq_dict.items():
                if freq_dict[num] != 0 and num not in row:
                    row.append(num)
                    freq_dict[num] -= 1

        return matrix
