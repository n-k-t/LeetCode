class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Create a storage list and another to store the continuous number ranges.
        storage = []
        temp = []

        # Iterate through the list, adding all numbers with a difference of one to 
        # the temporary tracker. If a number does not have a difference of one, then 
        # the current range is saved as a specific string '{start}->{stop}' within the 
        # main storage list, the temporary one is emptied, then the current value is 
        # appended.
        for i in range(len(nums)):
            if not temp:
                temp.append(nums[i])
            elif nums[i] - temp[-1] == 1:
                temp.append(nums[i])
            else:
                if len(temp) == 1:
                    storage.append(f'{temp[0]}')
                else:
                    storage.append(f'{temp[0]}->{temp[-1]}')
                temp.clear()
                temp.append(nums[i])
        
        # Empty the list to remove the last value(s).
        if len(temp) == 1:
            storage.append(f'{temp[0]}')
        elif len(temp) > 1:
            storage.append(f'{temp[0]}->{temp[-1]}')

        # Return the final list of the number ranges.
        return storage