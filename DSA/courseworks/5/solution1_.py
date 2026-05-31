class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def build_list(arr):
    head = ListNode(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = ListNode(x)
        curr = curr.next
    return head

def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

def reverseBetween(head, left, right):
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next

    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next


print("Enter linked list elements (space-separated):")
arr = list(map(int, input().split()))
print("Enter left position:")
left = int(input())
print("Enter right position:")
right = int(input())

head = build_list(arr)
head = reverseBetween(head, left, right)

print_list(head)