class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # Storage array.
        mat_l = len(mat)
        storage = []
        
        # Handle the beginning cases. Though, these should work with 
        # the method used below.
        if mat_l == 1:
            return mat[0][0]
        if mat_l == 2:
            return (sum(mat[0]) + sum(mat[1]))

        # Iterate through the length of the matrix, storing the right and 
        # left diagonal elements. If the matrix is of odd length, only 
        # count the middle element once.
        for i in range(mat_l):
            if mat_l % 2 == 1:
                if i == mat_l // 2:
                    storage.append(mat[i][i])
                else:
                    storage.append(mat[i][i])
                    storage.append(mat[i][mat_l - i - 1])
            else:
                storage.append(mat[i][i])
                storage.append(mat[i][mat_l - i - 1])

        # Return the sum of the storage array.
        return sum(storage)