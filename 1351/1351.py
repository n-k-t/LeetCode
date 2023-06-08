class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Initialize the matrix dimensions and a count to track the number of 
        # negative numbers in the matrix.
        len_m = len(grid)
        len_n = len(grid[0])
        count = 0

        # Because each row of the matrix is sorted, traverse each row from 
        # right to left, incrementing the count each time a negative number 
        # is encountered. When a positive number (or 0) is encountered, break 
        # the loop and move onto the next row.
        for i in range(len_m):
            for j in range(1, len_n + 1):
                if grid[i][-j] < 0:
                    count += 1
                else:
                    break
        
        # Return the number of negative numbers in the sorted matrix.
        return count