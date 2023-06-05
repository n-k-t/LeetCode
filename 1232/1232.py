#### Attempt 1 ####

'''
Kept track of the slope for all points in relation to the first in the list. Have an early exit for 
two points (always a line). Also, account for an edge case where the line is vertical (the x component 
has no change), storing only the x component and setting its value to None. If all cases are True in 
the loop, then True is returned.
'''

# class Solution:
#     def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
#         len_c = len(coordinates)

#         if len_c == 2:
#             return True

#         if (coordinates[1][0] - coordinates[0][0]) == 0:
#             slope = None
#         else:
#             slope = ((coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0]))

#         for i in range(2, len_c):
#             if (coordinates[i][0] - coordinates[0][0]) == 0:
#                 slope_temp = None
#             else:
#                 slope_temp = ((coordinates[i][1] - coordinates[0][1]) / (coordinates[i][0] - coordinates[0][0]))
#             if slope != slope_temp:
#                 return False
        
#         return True


#### Attempt 2 ####

'''
A very similar approach to above, except we are multiplying the x and y components of opposite slopes. 
I also removed the test case at the front. A little bit faster, but not tremendously.
'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Initialize the first x and y components of the slope.
        x_s = (coordinates[1][0] - coordinates[0][0])
        y_s = (coordinates[1][1] - coordinates[0][1])

        # Compare the product of opposite components in other points, if not equal then return False.
        for i in range(2, len(coordinates)):
            if (y_s * (coordinates[i][0] - coordinates[0][0])) != (x_s * (coordinates[i][1] - coordinates[0][1])):
                return False
        
        # If all cases pass, then return True.
        return True