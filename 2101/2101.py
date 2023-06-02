class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Run depth first search on the bomb graph, recording those bombs 
        # that are caught in the chain reaction.
        def dfs(bomb, b_exploded, b_dict):
            for i in b_dict[bomb]:
                if i not in b_exploded:
                    b_exploded.append(i)
                    dfs(i, b_exploded, b_dict)

        # Initialize the length of the bomb list, a storage for the maximum 
        # number of bombs set off, and a dictionary for the bombs caught 
        # in a given bomb's explosion.
        len_b = len(bombs)
        max_det = 0
        bomb_dict = dict((i, []) for i in range(len_b))

        # Iterate through all bombs twice (O(n^2)) and record all of those 
        # that are set off by the key's detonation.
        for i in range(len_b):
            for j in range(len_b):
                x = bombs[i][0] - bombs[j][0]
                y = bombs[i][1] - bombs[j][1]
                if bombs[i][2] >= math.sqrt(x**2 + y**2):
                    bomb_dict[i] += [j]

        # Run depth first search, starting from each bomb. Record the 
        # greatest number of bombs set off from a single starting 
        # explosion.
        for i in range(len_b):
            exploded = [i]
            dfs(i, exploded, bomb_dict)
            max_det = max(max_det, len(exploded))
        
        # Return the greatest number of explosions.
        return max_det