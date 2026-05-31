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


# Find second last element
def second_last(head):
    # Edge cases
    if head is None or head.next is None:
        return None

    current = head

    while current.next.next:
        current = current.next

    return current.data


# Print list
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("NULL")


# ----------- Test Case 1 -----------
head1 = None
for val in [2, 4, 6, 8, 33, 67]:
    head1 = insert(head1, val)

print_list(head1)
print("Second Last:", second_last(head1))


# ----------- Test Case 2 -----------
head2 = None
for val in [1, 2, 3, 4, 5]:
    head2 = insert(head2, val)

print_list(head2)
print("Second Last:", second_last(head2))