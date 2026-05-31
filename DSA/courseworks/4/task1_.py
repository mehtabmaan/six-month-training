class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to insert at beginning
def insert_at_beginning(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node  # new head

# Function to create linked list from input
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

def print_list(head):
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None")

# ---- USER INPUT ----
elements = list(map(int, input("Enter linked list elements (space-separated): ").split()))
value = int(input("Enter value to insert at beginning: "))

# Create list
head = create_linked_list(elements)

# Insert at beginning
head = insert_at_beginning(head, value)

# Output
print("Updated Linked List:")
print_list(head)