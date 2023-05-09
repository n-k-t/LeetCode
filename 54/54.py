class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Get the dimensions of the input matrix.
        m = len(matrix)
        n = len(matrix[0])

        # Define the initial bounds for traversal.
        top = 0
        bot = m - 1
        left = 0
        right = n - 1

        # Track the direction (really the operation) that will be performed 
        # for the traversal.
        direction = 0

        # Initialize a storage array.
        storage = []

        # A loop that runs while the conditions (bounds) are met: if the top 
        # does not pass the bottom and the left does not pass the right. 
        #### **NOTE:** it is key that elif statements are used here as this 
        #### allows the while loop to check the conditions and end on the 
        #### correct iteration. Otherwise, it is possible to return extras.
        while(top <= bot and left <= right):
            # Traverse the current top row using direction 0.
            if direction == 0:
                for i in range(left, right + 1):
                    storage.append(matrix[top][i])
                # Increment the top row.
                top += 1
                
                # Change the direction.
                direction = 1

            # Repeat for each direction while the conditions are satisfied.
            elif direction == 1:
                for i in range(top, bot + 1):
                    storage.append(matrix[i][right])
                
                right -= 1

                direction = 2

            elif direction == 2:
                for i in range(right, left - 1, -1):
                    storage.append(matrix[bot][i])
                
                bot -= 1

                direction = 3

            elif direction == 3:
                for i in range(bot, top - 1, -1):
                    storage.append(matrix[i][left])
                
                left += 1

                direction = 0
        
        # Return the matrix as a clockwise spiral vector.
        return storage