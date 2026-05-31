import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    # Dummy node to track the head of the merged list
    dummy = ListNode(0)
    current = dummy
    heap = []
    
    # Push the head of each list into the heap
    # We include 'i' (index) to handle cases where node values are identical
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
            
    while heap:
        val, i, node = heapq.heappop(heap)
        
        # Connect the smallest node to our result list
        current.next = node
        current = current.next
        
        # If there is a next node in the current list, push it to heap
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
            
    return dummy.next