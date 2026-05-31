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

def reverse(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def max_twin_sum(head):
    slow = head
    fast = head
   
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    second_half = reverse(slow)

    first_half = head
    max_sum = 0
    
    while second_half:
        curr_sum = first_half.data + second_half.data
        max_sum = max(max_sum, curr_sum)
        first_half = first_half.next
        second_half = second_half.next
    
    return max_sum

# ---- USER INPUT ----
elements = list(map(int, input("Enter linked list elements (even length): ").split()))

head = create_linked_list(elements)

result = max_twin_sum(head)

print("Maximum Twin Sum:", result)