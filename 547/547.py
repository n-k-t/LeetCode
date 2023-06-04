class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Run depth first search for the given city and mark all of its 
        # connecting cities as visited.
        def dfs(connections, city, visited):
            visited[city] = True
            for i in range(len(connections[city])):
                if connections[city][i] == 1 and visited[i] == False:
                    dfs(connections, i, visited)
            return

        # Initialize a length variable, tracking array, and counter to 
        # track the number of provinces.
        len_c = len(isConnected)
        visited = [False] * len_c
        num_provinces = 0

        # Handle the case early where we are only given one city.
        #### NOTE: This is unnecessary.
        if len_c == 1:
            return 1

        # Iterate the city connections, running DFS when the city has 
        # not been visited before. The counter is incremented each time 
        # that DFS is performed.
        for i in range(len_c):
            if visited[i] == False:
                num_provinces += 1
                dfs(isConnected, i, visited)
            else:
                continue

        # Return the number of provinces.
        return num_provinces