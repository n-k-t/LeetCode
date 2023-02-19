# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Check if the binary tree is empty.
        if root is None:
            return []
        
        # Create the zig-zag list, node storage list, node value
        # storage list, layer tracker, and how many elements that
        # are left to pop.
        zig_zag = []
        node_store = [root]
        val_store = []
        layer = 0
        to_pop = 1

        # Call the function.
        current_level(zig_zag, node_store, val_store, layer, to_pop)

        return zig_zag

# Recursive function to traverse the binary tree layer-by-layer, 
# from left-to-right and vice-versa at the depth increases.
def current_level(zz_hold, node_store, val_store, layer, to_pop):
    # Check if we are at either layer zero or an even one.
    if layer % 2 == 0:
        # Append the child nodes from right to left.
        if node_store[0].right:
            node_store.append(node_store[0].right)
        if node_store[0].left:
            node_store.append(node_store[0].left)

        # Store the value, pop the node, and decrement the 
        # popping tracker.
        val_store.insert(0, node_store[0].val)
        node_store.pop(0)
        to_pop -= 1
    
    # Check if we are at an odd layer, repeat the above but 
    # insert at the start instead of append.
    if layer % 2 == 1:
        if node_store[0].right:
            node_store.append(node_store[0].right)
        if node_store[0].left:
            node_store.append(node_store[0].left)

        val_store.append(node_store[0].val)
        node_store.pop(0)
        to_pop -= 1
    
    # Update parameters when the popping tracker falls to 0.
    if to_pop == 0:
        zz_hold.append(val_store)
        val_store = []
        to_pop = len(node_store)
        print(to_pop)
        layer += 1
    
    # End recursion if the list is empty, otherwise go deeper.
    if not node_store:
        return
    else:
        current_level(zz_hold, node_store, val_store, layer, to_pop)