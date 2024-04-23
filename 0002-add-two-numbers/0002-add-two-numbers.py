# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node as the head of the result linked list
        head = ListNode()
        current = head   # Set current node to the head
        carry = 0

        # Loop until both linked lists and carry are empty
        while l1 or l2 or carry:
            #If l1 or l2 exist initialize it's value if no initialize 0.
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            # Calculate the total sum of current digits and carry
            total = l1_value + l2_value + carry
            # Create a new node to hold the least significant digit of the total sum
            current.next = ListNode(total % 10)
            # Update carry for the next iteration
            carry = total // 10

            #Move list pointers forward, if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # Move current pointer to the next node
            current = current.next 
        # Return the next node after the dummy node (head) in the new LL, which is the actual result
        return head.next

        #Note 
        # we do this l1_value = l1.val if l1 else 0, 465 + 3427 in these cases 
        # because one of the list might have additional digits. 
        
        #Why total%10 ? 
        # We do this to find the least significant digit of total bc we can't add two digit numbers in the node.
        #This operation is performed because the sum of two digits may exceed 9, resulting in a two-digit number. 
        #For example lets say the total is 15, we first need to add 5 to the node and 1 as carry to the next node.
        # Now to do this we do need to do two operations(total and carry), total%10, ie.15%10=5 and to calculate carry, 
        # carry = total // 10 
        # carry = 15 // 10 
        # carry = 1
        # carry is added to the next nodes
        # Now we move the list pointers(l1,l2,carry) to the next node