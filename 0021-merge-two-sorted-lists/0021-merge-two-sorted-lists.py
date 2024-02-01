# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
                
        head = ListNode()  # Create a new node and we call it head.
        current = head     # Create a pointer called current and point it to head.

        # Iterate while both lists are not Null.
        while list1 and list2:
            if list1.val < list2.val:  # Decide which list to point to based on the comparison of node values.
                current.next = list1 # Point the current pointer to list1.
                list1 = list1.next # Move list1's value to the next node on the linked list.
            else:
                current.next = list2  # Point the current pointer to list2.
                list2 = list2.next # Move list2's value to the next node on the linked list.
            current = current.next # At the end of each loop move c ---> to the respective pointed node.

        current.next = list1 or list2 # When one of the LL reaches Null, we need to point the current pointer to 
#the LL which has remaining values. Basically we're pointing the current pointer which is not null.
  
        return head.next # Finally point to the starting node, which is head.next.
        