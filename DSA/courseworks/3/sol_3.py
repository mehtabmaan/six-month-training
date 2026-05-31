class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    # Dummy head simplifies the logic for creating the result list
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    # Continue as long as there are nodes to process or a carry remains
    while l1 or l2 or carry:
        # Get values from nodes, or 0 if the list has ended
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        new_digit = total % 10
        
        # Add to the result list
        current.next = ListNode(new_digit)
        current = current.next
        
        # Move pointers forward
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        
    return dummy.next