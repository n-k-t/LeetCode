class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # Sort the array and intialize the difference between the first two values.
        arr.sort()
        difference = arr[1] - arr[0]

        # Iterate through all subsequent differences and return False if any of them 
        # are not equal to the one calculated above.
        for i in range(1, len(arr) - 1):
            if difference != arr[i + 1] - arr[i]:
                return False
        
        # If all test cases pass, then return True.
        return True