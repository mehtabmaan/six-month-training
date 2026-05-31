class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertBeforeMiddle(head: ListNode, value_to_insert: int) -> ListNode:
    # Base Case: If the list is empty, create a single node and return it
    if not head:
        return ListNode(value_to_insert)
    
    # Base Case: If there is only one node, the new node becomes the new head
    if not head.next:
        return ListNode(value_to_insert, next=head)

    slow = head
    fast = head
    prev = None

    # Traverse to find the middle node
    # The condition 'fast.next.next' ensures we pick the first middle in even-length lists
    while fast and fast.next and fast.next.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Create the new node
    new_node = ListNode(value_to_insert)

    # If prev is None, it means we are inserting right at the head
    if not prev:
        new_node.next = head
        return new_node
    else:
        # Insert the new node between prev and slow
        prev.next = new_node
        new_node.next = slow

    return head


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
    print("->".join(nodes))

# --- Running the Test Cases ---

# Test Case 1: Odd number of nodes
print("Test Case 1 (Odd Length):")
list1 = build_linked_list([1, 2, 3, 4, 5])
print("Original List: ", end="")
print_linked_list(list1)

updated_list1 = insertBeforeMiddle(list1, 9)
print("Updated List:  ", end="")
print_linked_list(updated_list1) 
# Expected Output: 1->2->9->3->4->5

print("-" * 40)

# Test Case 2: Even number of nodes 
# Note: The second test case prompt had a slight typo in its output example text 
# (showing a 12 out of nowhere), but the goal is to insert 8 right before the first middle (7).
print("Test Case 2 (Even Length):")
list2 = build_linked_list([11, 10, 9, 7, 6, 5, 4, 3, 2, 1])
print("Original List: ", end="")
print_linked_list(list2)

updated_list2 = insertBeforeMiddle(list2, 8)
print("Updated List:  ", end="")
print_linked_list(updated_list2)
# Expected Output: 11->10->9->8->7->6->5->4->3->2->1
