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

def oddEvenList(head):
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even   

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head


print("Enter linked list elements (space-separated): ")
arr = list(map(int, input().split()))

head = build_list(arr)
head = oddEvenList(head)

print_list(head)