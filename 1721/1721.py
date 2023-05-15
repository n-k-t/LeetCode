#### Attempt 1 ####

'''
My first at incorporating a lag variable and incrementing it each time did not work. 
I ended up going back to the drawing board and implementing a simple solution that 
iterates throughout the entirety of the singly-linked list and stores all of the 
values in an array. Then, I iterate though the linked list again, updating the 
values of the nodes that were specified. I return the head of the linked list at 
the end.
'''

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         storage = []
#         stop = True
#         curr = head

#         while stop:
#             storage.append(curr.val)
#             if curr.next:
#                 curr = curr.next
#             else:
#                 stop = False
        
#         curr = head
#         len_s = len(storage)

#         for i in range(len_s):
#             if i == k - 1:
#                 curr.val = storage[len_s - k]
#             if i == len_s - k:
#                 curr.val = storage[k - 1]
#             curr = curr.next
        
#         return head


#### Attempt 2 ####

'''
Looked at some other solutions and found a better implementation of my initial attempt 
that I had made before above's submission. I have a front and rear tracker initialized 
at the head of the linked list, then I increment the front until k is reached. Once it 
is, I set a storage node to track that location. Then, I traverse the linked list 
using both the front and rear trackers (now spaced by k), and swap the value of the 
temporary front tracker and rear tracker (once the end is reached).
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        front = head
        rear = head

        for i in range(k - 1):
            front = front.next
        
        left_storage = front

        while front.next:
            rear = rear.next
            front = front.next

        left_storage.val, rear.val = rear.val, left_storage.val

        return head 
