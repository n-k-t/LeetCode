#### Attempt 1 ####

'''
The principle idea is that the root nodes will have no incoming edges. This means that 
if we remove all nodes with incoming edges, then we can find the minimum nodes that 
allow us to reach all other nodes.

Create a dictionary to store all source nodes (of count n). Then, iterate throughout the 
edge list and track all destination nodes. Check the set (deleting duplicates) of 
destination nodes and delete the dictionary entry if it is present in the set. 
Return 
'''

# class Solution:
#     def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
#         constructor = [(i, []) for i in range(n)]
#         connections = dict(constructor)
#         storage = []

#         for i in edges:
#             storage.append(i[1])
        
#         for i in set(storage):
#             del connections[i]
        
#         return [i for i in connections]


#### Attempt 2 ####

'''
A faster implementation where we don't have to track/copy into memory the destination nodes. 
Instead, we have a list of booleans that allows us to track those that have destinations. 
We return a list of the indices (nodes) that were never the destination.
'''

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        storage = [True for _ in range(n)]

        for i in edges:
            storage[i[1]] = False
        
        return [i for i in range(n) if storage[i]]