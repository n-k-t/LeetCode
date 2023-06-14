# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        # Define a breadth-first search that tracks each node as it is 
        # visited and return the visited list.
        def bfs(root):
            stack = [root]
            visited = []
            while len(stack) > 0:
                temp = stack.pop(0)
                visited.append(temp.val)
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)
            return visited

        # Perform BFS on the root node and sort the resulting list.
        sorted_nodes = bfs(root)
        sorted_nodes.sort()

        # Set the minimum difference to that between the first and last 
        # node in the sorted list (largest gap).
        minimum_diff = sorted_nodes[-1] - sorted_nodes[0]

        # Iterate through the list to find the minimum difference between 
        # two nodes in the binary search tree.
        for i in range(0, len(sorted_nodes) - 1):
            if sorted_nodes[i + 1] - sorted_nodes[i] < minimum_diff:
                minimum_diff = sorted_nodes[i + 1] - sorted_nodes[i]

        # Return the minimum difference.
        return minimum_diff