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


# Reverse linked list
def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


# Print list
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("NULL")


# ----------- Test Case 1 -----------
head1 = None
for val in [1, 2, 3, 4]:
    head1 = insert(head1, val)
    
print("Original:", end=" ")
print_list(head1)

head1 = reverse_list(head1)

print("Reversed:", end=" ")
print_list(head1)


# ----------- Test Case 2 -----------
head2 = None
for val in [1, 2, 3, 4, 5]:
    head2 = insert(head2, val)

print("Original:", end=" ")
print_list(head2)

head2 = reverse_list(head2)

print("Reversed:", end=" ")
print_list(head2)