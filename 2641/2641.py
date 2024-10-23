# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0

        queue = [root]

        # Perform a layer-wise BFS, getting the total sum of all nodes on that layer and tracking the sum for all children of 
        # a parent. Then, update the children's value by subtracting the children total from the overall total.
        while len(queue) > 0:
            children = []
            children_sum = []

            total = 0

            for parent in queue:
                temp_sum = 0

                if parent.left:
                    children.append(parent.left)
                    temp_sum += parent.left.val
                if parent.right:
                    children.append(parent.right)
                    temp_sum += parent.right.val
                
                children_sum.append(temp_sum)
                total += temp_sum
            
            for ind, parent in enumerate(queue):
                if parent.left:
                    parent.left.val = total - children_sum[ind]
                if parent.right:
                    parent.right.val = total - children_sum[ind]

            queue = children
        
        return root