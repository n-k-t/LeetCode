class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # Find the length of each list.
        l_n1 = len(nums1)
        l_n2 = len(nums2)

        # Initialize a matrix of zeros with side length equal to the length of 
        # each list plus one. This is essentially a larger adjacency matrix 
        # that allows us to keep track of the lines drawn between indices.
        storage = [[0 for _ in range(l_n2 + 1)] for _ in range(l_n1 + 1)]

        # In order to find the solution with the most non-crossing lines drawn, 
        # we will take a dynamic programming approach. We begin with zero elements 
        # from each of the arrays, meaning the first row and column are all zero as 
        # we may not draw lines between no points. Next, we incrementally add elements 
        # back to each list and compare whether or not they are equal. If they are, we 
        # add one to the cell's upper left neighbor. If they are not, then we take the 
        # maximum value in its upper or left-most neighbor. This process accounts for 
        # other connections made in smaller segments of the two lists and builds the 
        # one with the most connections by utilizing the previous connections in 
        # the sub-lists. Using the diagonal value when the numbers match prevents a 
        # duplicate being drawn (if the sequential numbers are identical) as neither 
        # list's value were "discovered" yet in the diagonal cell.
        for i in range(l_n1):
            for j in range(l_n2):
                if nums1[i] == nums2[j]:
                    storage[i + 1][j + 1] = storage[i][j] + 1
                else:
                    storage[i + 1][j + 1] = max(storage[i + 1][j], storage[i][j + 1])

        # Return the last element of the matrix.
        return storage[-1][-1]