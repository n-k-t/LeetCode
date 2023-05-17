#### Attempt 1 ####

'''
Iterate through the linked list once and write each value to an array. 
Then, I add the corresponding element and its twin (index from the end) 
to the halfway point (note that all linked lists have an even number of 
elements). I return the minimum sum of all twin values.
'''

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         storage = []

#         while head != None:
#             storage.append(head.val)
#             head = head.next
        
#         num_its = int(len(storage) / 2)
#         max_twin_sum = 0

#         for i in range(num_its):
#             if (storage[i] + storage[(-i - 1)]) > max_twin_sum:
#                 max_twin_sum = storage[i] + storage[(-i - 1)]
        
#         return max_twin_sum


#### Attempt 2 ####

'''
A second method that finds the mid-point of the linked list, reverses the 
second half, and then returns the max twin sum. One can find the midpoint 
of a linked list by having two trackers, one moves at twice the speed of 
the other meaning that when the faster one reaches the end, then the slower 
one is in the middle. Then, we can use a two pointers (and a temporary third) 
to reverse the second half of the list. The second tracker is set to None 
at the start (signalling the end of the reversed list) and the temporary 
variable is a duplicate of the main (initial midpoint) tracker. The main 
tracker moves to the next node along the initial linked list, the temp 
node points to the previous tracker, and then the previous tracker becomes 
the temp node (essentially creating its own reversed linked list). This 
continues until the entire second half of the linked list is encompassed 
by the previous tracker (head of the new linked list).
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Set the slow and fast trackers to the head node.
        slow = fast = head

        # Find the midpoint of the initial linked list.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Initialize the previous tracker as None.
        prev = None

        # Create a reversed linked list for the second half.
        while slow:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp
        
        # Create a max twin sum tracker.
        max_twin_sum = 0

        # Iterate through all options and find the maximum sum.
        while prev:
            max_twin_sum = max(max_twin_sum, head.val + prev.val)
            head = head.next
            prev = prev.next
        
        # Return the maximum twin sum.
        return max_twin_sum