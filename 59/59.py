class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # A n x n matrix of zeros to build the output in.
        storage = [[0 for i in range(n)] for i in range(n)]

        # Parameters for a matrix traversal in spiral order.
        top = 0
        bot = n - 1
        left = 0
        right = n - 1

        # Set the initial direction of movement. 
        direction = 0

        # Set the initial value to be placed within the matrix. 
        tracker_val = 1

        # Traverse the n x n matrix in the spiral manner (clockwise) 
        # and drop in the value for the tracker, incrementing it at 
        # each iteration.
        while(top <= bot and left <= right):
            if direction == 0:
                for i in range(left, right + 1):
                    storage[top][i] = tracker_val
                    tracker_val += 1

                top += 1
                direction = 1

            elif direction == 1:
                for i in range(top, bot + 1):
                    storage[i][right] = tracker_val
                    tracker_val += 1
                
                right -= 1
                direction = 2
            
            elif direction == 2:
                for i in range(right, left - 1, -1):
                    storage[bot][i] = tracker_val
                    tracker_val += 1
                
                bot -= 1
                direction = 3
            
            elif direction == 3:
                for i in range(bot, top - 1, -1):
                    storage[i][left] = tracker_val
                    tracker_val += 1
                
                left += 1
                direction = 0
        
        # Return the matrix. 
        return storage