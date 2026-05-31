class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle(head):
    # Edge case
    if head is None:
        return -1   # or None

    slow = head
    fast = head

    # Traverse using two pointers
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.data


# Helper function to insert at end
def insert(head, value):
    new_node = Node(value)

    if head is None:
        return new_node 

    temp = head
    while temp.next is not None:
        temp = temp.next

    temp.next = new_node
    return head


head = None
for val in [1, 2, 3, 4, 5]:
    head = insert(head, val)

print("Middle element is:", find_middle(head))

head = None 
for val in [2, 3, 4, 5]:
    head = insert(head, val)

print("Middle element is:", find_middle(head))