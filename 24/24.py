#### Attempt 1 ####

'''
A basic iteration method that swaps the position of each node pair (non-inclusive across pairs, 
i.e. 1,2 and 3,4 --> 2,3 and 1,4 are not included). It resets the head position, tracks two 
node pointers throughout the linked list, and swaps their position.
'''

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None:
#             return head
#         if head.next is None:
#             return head
        
#         front, back = head, head
#         count = 0

#         while front.next:
#             if count % 2 == 0:
#                 if front == head:
#                     front = front.next
#                     temp = front.next
#                     back.next = temp
#                     front.next = back
#                     head = front
#                     front = front.next
#                     count += 1
#                 else:
#                     front = front.next
#                     temp_f = front.next
#                     temp_b = back
#                     back = back.next
#                     back.next = temp_f
#                     temp_b.next = front
#                     front.next = back
#                     front = front.next
#                     count += 1
#             else:
#                 front = front.next
#                 count += 1
        
#         return head
    
#### Attempt 2 ####

'''
A recursive approach that resets the head to point two nodes ahead of its position 
and call the same function, placing the head further down the linked list. This is 
returned to re-route the head's connection, while the temporary variable acts as 
the connector node (to the back of the head) after the new head connection is made. 
If there are not enough positions (node values) after the function is called, then 
the head is returned.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head
        
        temp = head.next
        head.next = self.swapPairs(head.next.next)
        temp.next = head
        return temp