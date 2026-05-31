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
def reverse(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


# Add 1 to linked list
def add_one(head):
    # Step 1: reverse list
    head = reverse(head)

    curr = head
    carry = 1

    # Step 2: add 1
    while curr:
        sum_val = curr.data + carry

        curr.data = sum_val % 10
        carry = sum_val // 10

        # If no carry → stop early
        if carry == 0:
            break

        # If last node and still carry
        if curr.next is None and carry:
            curr.next = Node(carry)
            carry = 0
            break

        curr = curr.next

    # Step 3: reverse back
    head = reverse(head)

    return head


# Print list
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end="")
        temp = temp.next
    print()


# ----------- Test Case 1 -----------
head1 = None
for val in [1, 9, 9, 9]:
    head1 = insert(head1, val)

print("Input: ", end="")
print_list(head1)

head1 = add_one(head1)

print("Output:", end="")
print_list(head1)


# ----------- Test Case 2 -----------
head2 = None
for val in [3, 4, 5, 3]:
    head2 = insert(head2, val)

print("Input: ", end="")
print_list(head2)

head2 = add_one(head2)

print("Output:", end="")
print_list(head2)