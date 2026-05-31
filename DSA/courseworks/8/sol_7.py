class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: ListNode, k: int) -> ListNode:
    # Base cases: empty list, single node, or no rotation needed
    if not head or not head.next or k == 0:
        return head

    # Step 1: Calculate the length of the list and find the tail node
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Handle edge cases where k >= length
    k = k % length
    if k == 0:
        return head  # No rotation needed

    # Step 3: Link the tail to the head to form a circular loop
    tail.next = head

    # Step 4: Find the new tail node, which is at index (length - k)
    # We move (length - k) steps from the current head
    new_tail_steps = length - k
    new_tail = head
    for _ in range(new_tail_steps - 1):
        new_tail = new_tail.next

    # Step 5: The node next to the new tail becomes the new head
    new_head = new_tail.next
    
    # Break the circular loop
    new_tail.next = None

    return new_head


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

# Test Case 1: k = 4
print("Test Case 1:")
list1 = build_linked_list([10, 20, 30, 40, 50, 60])
print("Original List: ", end="")
print_linked_list(list1)

rotated_list1 = rotateRight(list1, 4)
print("Rotated by 4:  ", end="")
print_linked_list(rotated_list1)
# Expected Output: 30->40->50->60->10->20

print("-" * 40)

# Test Case 2: k = 2
print("Test Case 2:")
list2 = build_linked_list([30, 40, 50, 60])
print("Original List: ", end="")
print_linked_list(list2)

rotated_list2 = rotateRight(list2, 2)
print("Rotated by 2:  ", end="")
print_linked_list(rotated_list2)
# Expected Output: 50->60->30->40