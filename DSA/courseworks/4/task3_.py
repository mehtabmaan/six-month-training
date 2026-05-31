class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list(elements):
    head = None
    tail = None
    for el in elements:
        new_node = Node(el)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

def merge_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next

def print_list(head):
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None")

# ---- USER INPUT ----
list1 = list(map(int, input("Enter elements of list1 (sorted): ").split()))
list2 = list(map(int, input("Enter elements of list2 (sorted): ").split()))

head1 = create_linked_list(list1)
head2 = create_linked_list(list2)

merged_head = merge_lists(head1, head2)

print("Merged Linked List:")
print_list(merged_head)