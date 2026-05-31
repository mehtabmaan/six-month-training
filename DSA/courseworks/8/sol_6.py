class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteLastOccurrence(head: ListNode, target: int) -> ListNode:
    # Use a dummy node to seamlessly handle deleting the head node
    dummy = ListNode(0)
    dummy.next = head
    
    curr = head
    prev = dummy
    
    # Track the node right before the last occurrence of the target
    last_match_prev = None
    
    # Step 1: Traverse the list to find the last occurrence
    while curr:
        if curr.val == target:
            last_match_prev = prev
        prev = curr
        curr = curr.next
        
    # Step 2: If a match was found, delete it
    if last_match_prev is not None:
        # Skip over the target node
        last_match_prev.next = last_match_prev.next.next
        
    return dummy.next


# --- Helper functions to build and print the linked list ---
def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    nodes = []
    curr = head
    while curr:
        nodes.append(str(curr.val))
        curr = curr.next
    nodes.append("NULL")
    print(" --> ".join(nodes))


# --- Running the Test Cases ---

# Test Case 1: Deleting last occurrence of 4
print("Test Case 1:")
list1 = build_linked_list([1, 2, 3, 4, 5, 4, 4])
print("Created Linked list:      ", end="")
print_linked_list(list1)

updated_list1 = deleteLastOccurrence(list1, 4)
print("List after deletion of 4: ", end="")
print_linked_list(updated_list1)

print("-" * 50)

# Test Case 2: Deleting last occurrence of 445
print("Test Case 2:")
list2 = build_linked_list([11, 32, 123, 344, 445, 484, 534])
print("Created Linked list:        ", end="")
print_linked_list(list2)

updated_list2 = deleteLastOccurrence(list2, 445)
print("List after deletion of 445: ", end="")
print_linked_list(updated_list2)