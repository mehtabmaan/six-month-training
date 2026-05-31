class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nodes(head):
    # Step 1: Reverse the linked list
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    # Step 2: Traverse and remove nodes smaller than the max seen so far
    curr = prev  # prev is now the new head
    max_val = -1
    new_head_prev = None
    dummy = ListNode(0)
    temp = dummy

    while curr:
        if curr.val >= max_val:
            max_val = curr.val
            # Build the filtered list (still reversed)
            temp.next = ListNode(curr.val)
            temp = temp.next
        curr = curr.next

    # Step 3: Reverse back to restore original order
    res_prev = None
    res_curr = dummy.next
    while res_curr:
        res_nxt = res_curr.next
        res_curr.next = res_prev
        res_prev = res_curr
        res_curr = res_nxt
        
    return res_prev

# --- User Input Handling ---
def create_linked_list(arr):
    if not arr: return None
    head = ListNode(int(arr[0]))
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(int(val))
        curr = curr.next
    return head

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res))

if __name__ == "__main__":
    user_input = input("Enter node values separated by space (e.g., 5 2 13 3 8): ").split()
    head = create_linked_list(user_input)
    
    result = remove_nodes(head)
    
    print("Modified List:")
    print_list(result)