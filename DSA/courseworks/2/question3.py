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


# Remove duplicates (sorted list)
def remove_duplicates(head):
    current = head

    while current and current.next:
        if current.data == current.next.data:
            # Skip duplicate node
            current.next = current.next.next
        else:
            current = current.next

    return head


# Print list
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("NULL")


# ----------- Test Case 1 -----------
head1 = None
for val in [11, 11, 11, 13, 13, 20]:
    head1 = insert(head1, val)

print("Original:", end=" ")
print_list(head1)

head1 = remove_duplicates(head1)

print("After Removing Duplicates:", end=" ")
print_list(head1)


# ----------- Test Case 2 -----------
head2 = None
for val in [10, 15, 15, 15, 20, 20, 20, 23, 25, 25]:
    head2 = insert(head2, val)

print("Original:", end=" ")
print_list(head2)

head2 = remove_duplicates(head2)

print("After Removing Duplicates:", end=" ")
print_list(head2)