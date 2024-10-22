# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        max_depth = 0
        cur_depth = 0
        sum_track = [0] * 10**5

        max_depth = self.dfs(root, sum_track, cur_depth, max_depth)

        if k - 1 > max_depth:
            return -1
        else:
            sum_track.sort(reverse = True)
            return sum_track[k - 1]

    # Perform depth-first search, tracking the sum, current depth, and max depth. Return the max depth.
    def dfs(self, root: TreeNode, sum_track: List[int], cur_depth: int, max_depth: int) -> int:
        if root is None:
            return max_depth

        if cur_depth > max_depth:
            max_depth = cur_depth

        sum_track[cur_depth] += root.val
        max_depth = self.dfs(root.left, sum_track, cur_depth + 1, max_depth)
        max_depth = self.dfs(root.right, sum_track, cur_depth + 1, max_depth)

        return max_depth