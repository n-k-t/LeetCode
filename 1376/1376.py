class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Create a depth-first traversal of the company hierarchy that is created further down. It 
        # iterates over all employess connected to the lead of the group, going deeper each 
        # iteration and tracking the maximum amount of time required to inform all of the 
        # employees. It adds the manager's informing time at the very end and returns it.
        def dfs(tree, lead_person, times):
            max_time = 0
            for i in tree[lead_person]:
                max_time = max(max_time, dfs(tree, i, times))
            return max_time + times[lead_person]

        # Initialize the length of the employee list. The defaultdict() is a dictionary that does 
        # not throw an error, instead it creates a default instance of a given type (list in this 
        # case) and proceeds to run. This helps deal with cases where the dictionary is actually 
        # empty or the value is a leaf node.
        len_m = len(manager)
        hierarchy = defaultdict(list)

        # Create the tree, tracking the indices of the parent and each child (and so on).
        for i in range(len_m):
            if manager[i] == -1:
                continue
            if manager[i] not in hierarchy:
                hierarchy[manager[i]] = [i]
            else:
                hierarchy[manager[i]] += [i]
        
        # Return the DFS of the company hierarchy.
        return dfs(hierarchy, headID, informTime)