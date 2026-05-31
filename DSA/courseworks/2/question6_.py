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


# Add two linked lists
def add_lists(l1, l2):
    # Step 1: reverse both lists
    l1 = reverse(l1)
    l2 = reverse(l2)

    carry = 0
    result = None

    # Step 2: add digits
    while l1 or l2 or carry:
        sum_val = carry

        if l1:
            sum_val += l1.data
            l1 = l1.next

        if l2:
            sum_val += l2.data
            l2 = l2.next

        # create new node
        new_node = Node(sum_val % 10)
        carry = sum_val // 10

        # insert at front (to avoid reversing later)
        new_node.next = result
        result = new_node

    return result


# Print list
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("NULL")


# ----------- Test Case 1 -----------
l1 = None
for val in [5, 6, 3]:
    l1 = insert(l1, val)

l2 = None
for val in [8, 4, 2]:
    l2 = insert(l2, val)

print("List1:", end=" ")
print_list(l1)
print("List2:", end=" ")
print_list(l2)

result = add_lists(l1, l2)

print("Result:", end=" ")
print_list(result)


# ----------- Test Case 2 -----------
l1 = None
for val in [7, 5, 9, 4, 6]:
    l1 = insert(l1, val)

l2 = None
for val in [8, 4]:
    l2 = insert(l2, val)

print("List1:", end=" ")
print_list(l1)
print("List2:", end=" ")
print_list(l2)

result = add_lists(l1, l2)

print("Result:", end=" ")
print_list(result)