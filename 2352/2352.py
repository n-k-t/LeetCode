class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Find the length, take the transpose of the matrix, and initialize a 
        # tracking count variable.
        len_g = len(grid)
        transpose = [[grid[j][i] for j in range(len_g)] for i in range(len_g)]
        equality_count = 0

        # Iterate through all possible row and column pairs and record the 
        # number of times they are exactly equal. O(N^2).
        for i in grid:
            for j in transpose:
                if i == j:
                    equality_count += 1

        # Return the number of rows and columns that are equal.
        return equality_count