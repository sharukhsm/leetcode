# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head  # we initialize fast to head, bc it should start at the first node.

        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if (
                head is fast # is in python check the momory location and not the values.
            ):  
                return True
        return False


# In this preble we use the Tortoise and Hare Algorithm.
# Create two pointers head and fast. The head pointer moves one step in the LL. The fast pointer moves two step in the LL.
# During the iteration these two pointers should meet each other at one point. If it does meet then there is a cycle and we return True. If it isn't a cycle, Fast would have reached the end of the LL at some point and either Fast or Fast.next would have been null, so we would have broken out of the while loop and we return false.

#Remember, we are checking the memory address of head and fast and not their actual values, so we use 'is' in python.