class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    # If the list is empty or has only one node, no duplicates possible
    if not head:
        return head
    
    current = head
    
    # Traverse until the second to last node
    while current and current.next:
        if current.val == current.next.val:
            # Duplicate found: skip the next node
            current.next = current.next.next
        else:
            # No duplicate: move the pointer forward
            current = current.next
            
    return head