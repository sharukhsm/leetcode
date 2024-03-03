# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
                
        head = ListNode()  # Create a new node and we call it head.
        current = head     # Create a pointer called current and point it to head.

        
        while list1 and list2:         # Iterate while list1 and list2 are not Null.
            if list1.val < list2.val:  # Decide which list to point to based on the comparison of node values.
                current.next = list1   # POINTING the current pointer to list1.
                list1 = list1.next     # Move list1's value to the next node on the linked list.
            else:
                current.next = list2   # Point the current pointer to list2.
                list2 = list2.next     # Move list2's value to the next node on the linked list.
            current = current.next     # At the end of each loop move c ---> to the respective pointed node.

        current.next = list1 or list2  # When one of the LL reaches Null, we need to point the current pointer to 
#the LL which has remaining values. Basically we're pointing the current pointer which is not null.
  
        return head.next    # Finally point to the starting node, which is head.next.

# Note      
# current.next = list1 - we are pointing to list 1
# list1 = list1.next - we are moving list 1 value to the next value in the LL
# current = current.next - we are moving the current pointer to the pointed node

# Real life example:
# You could use this in scenarios where you have two sorted lists of elements and
#  you want to merge them into a single sorted list. Here's a real-life example:

# Let's say you are building a system that manages student records, and 
# each student's information is stored in a linked list node. The linked list is sorted based on
#  the student's roll number. Now, imagine you have two such linked lists, one for the first-year 
#  students and another for the second-year students. Each list is sorted based on the 
#  roll numbers of the students.

# At some point, you want to generate a consolidated list that contains all the student records, 
# maintaining the sorted order. This is where the mergeTwoLists function can be useful. 
# You can use it to merge the two sorted linked lists representing first-year and second-year 
# students into a single sorted linked list representing all students