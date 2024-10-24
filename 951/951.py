# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        q1 = deque([root1])
        q2 = deque([root2])

        # Iterate over each level of the tree (BFS) and then store the children and the parents. Then, sort the children
        # and verify that the resulting levels are equal.
        while len(q1) > 0:
            if len(q1) != len(q2):
                return False

            t1 = {}
            t2 = {}

            for _ in range(len(q1)):
                tl1 = q1.popleft()
                tl2 = q2.popleft()

                if tl1:
                    t1[tl1.val] = []
                    if tl1.left:
                        q1.append(tl1.left)
                        t1[tl1.val].append(tl1.left.val)
                    if tl1.right:
                        q1.append(tl1.right)
                        t1[tl1.val].append(tl1.right.val)
                    
                if tl2:
                    t2[tl2.val] = []
                    if tl2.left:
                        q2.append(tl2.left)
                        t2[tl2.val].append(tl2.left.val)
                    if tl2.right:
                        q2.append(tl2.right)
                        t2[tl2.val].append(tl2.right.val)
            
            if len(t1) != len(t2):
                return False
            
            for d1, d2 in zip(t1.values(), t2.values()):
                d1.sort()
                d2.sort()
            
            if t1 != t2:
                return False
        
        if len(q1) != len(q2):
                return False
        return True
