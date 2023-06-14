class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Initialize a dictionary to track the domino occurances.
        tracker = dict()
        
        # Iterate through all of the dominos, sorting them to eliminate 
        # any dependence on the order of the numbers; the lists are also 
        # converted to strings to make them hashable. Create a new key-
        # value pair with a value of 1 if the domino is not in the list, 
        # otherwise increment the key by one.
        for i in dominoes:
            i.sort()
            if str(i) not in tracker:
                tracker[str(i)] = 1
            else:
                tracker[str(i)] += 1

        # Create an equivalent counter.
        equivalent_count = 0

        # Iterate through the values, using a pairs equation to find 
        # all possible domino combinations and incrementing the counter 
        # by this value.
        for i in tracker.values():
            if i > 1:
                equivalent_count += i * ((i - 1) / 2)

        # Return the number of domino pairs.
        return int(equivalent_count)