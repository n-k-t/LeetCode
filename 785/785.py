'''
Began by looking for triangles and cases where the connections created loops that 
terminated in an "odd" manner -- where it could not be bipartite. But edge-cases 
kept on popping up, so BFS (or DFS) seemed like the best result. This method 
colors nodes as they are visited and checks for impossible combinations in a 
bipartite graph. If this is found, then a boolean is returned stating that it 
cannot be bipartite.
'''

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Store the graph length so it doesn't have to calculated more than once.
        len_g = len(graph)

        # Base colors are set neutrally for all nodes.
        coloring = [0 for _ in range(len_g)]

        # Create the queue for BFS.
        queue = []

        # Start BFS at each node in the graph (as there is no guarantee that all 
        # of them are singl/connected graphs, just that there are no repeated/ 
        # double connections). Check if the node has already been visited, if so 
        # then the graph (or subgraph) is already deemed bipartite. If not, then 
        # the root node is set to a color of "one" and added to the queue. A 
        # loop runs while the queue is not empty, traversing all nodes that are 
        # neighbors of the current front of the queue. The loop begins by popping 
        # the value at the front of the queue, then the neighbors are all checked; 
        # if they have a value of zero, then they are set the opposite color of 
        # the current node and added to the queue so all their neighbors may be 
        # visited. If the color of a neighbor matches the current node, then a 
        # 'False' boolean value is returned, indicating that the graph is not 
        # bipartite.
        for i in range(len_g):
            if coloring[i] != 0:
                continue
            
            coloring[i] = 1
            queue.append(i)

            while len(queue) != 0:
                current = queue.pop(0)
                for j in graph[current]:
                    if coloring[j] == 0:
                        coloring[j] = -coloring[current]
                        queue.append(j)
                    elif coloring[j] == coloring[current]:
                        return False

        # If the traversal runs successfully, then return True, indicating that 
        # the graph is bipartite.
        return True