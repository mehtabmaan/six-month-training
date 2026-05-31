class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Insert at end
def insert(head, value):
    new_node = Node(value)

    if head is None:
        return new_node

    temp = head
    while temp.next:
        temp = temp.next

    temp.next = new_node
    return head


# Delete middle node
def delete_middle(head):
    if head is None or head.next is None:
        return None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next

    return head


# Print list
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()


# ----------- Test Case 1 -----------
head1 = None
for val in [1, 2, 3, 4, 5]:
    head1 = insert(head1, val)

print("Original:", end=" ")
print_list(head1)

head1 = delete_middle(head1)

print("After Deletion:", end=" ")
print_list(head1)


# ----------- Test Case 2 -----------
head2 = None
for val in [2, 4, 6, 7, 5, 1]:
    head2 = insert(head2, val)

print("Original:", end=" ")
print_list(head2)

head2 = delete_middle(head2)

print("After Deletion:", end=" ")
print_list(head2)