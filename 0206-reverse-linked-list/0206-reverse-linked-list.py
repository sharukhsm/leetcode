# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        current = head

        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node
        return new_list



#Create a variable called new_list = None. This is because we're going to build the reverse list from the back to the front. And the "Last element of Every linked list is None".
#Create a variable called current and initialize it to the head node. Current is used to traverse the original list, while building the reverse list.
#Create a loop while current:, which will be true as long as current equals to None(this will happen while we traverse the reverse Link list at the end).
#Create a variable called next_node, in other words next node in the Likedlist and point it to the second element which is current.next, you will se why we do this at last.
#Now change the direction of the node by initializing current.next = new_list(which is none). Remember current.next is the arrow next to 1. Right now it points to the second node with a value of 2, we wanna point it to the reverse list that we are building.
# new_list = current. We update the new list variable to point at current, so that it always points to the new head of the reversed list.
#At this point we need to move the current node to the next node of the original list, so we can do the same process to the second node, but we ended up switching the link between the first and second node here current.next = new_list. But don't worry that's why we created the variable next_node and initialized it to the second node initially. So now we assign current = next_node
#The process happens for all the nodes.
#Now when we are at the last iteration, current equals none and when it hits the while loop -> it returns false and we exit the loop and just return the new_list, which points at the head of the new reversed linked list.
#This algorith runs O(n)time.



        