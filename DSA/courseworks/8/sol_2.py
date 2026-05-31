class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    # 1. If both trees are empty, they are identical
    if not p and not q:
        return True
    
    # 2. If one tree is empty and the other is not, they are not identical
    if not p or not q:
        return False
    
    # 3. Check if current data matches, and recursively check left and right subtrees
    return (p.val == q.val) and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# --- Helper function to build the tree from the test case format ---
def build_tree(nodes_list):
    if not nodes_list:
        return None
    root = TreeNode(nodes_list[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes_list):
        current = queue.pop(0)
        if i < len(nodes_list) and nodes_list[i] is not None:
            current.left = TreeNode(nodes_list[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes_list) and nodes_list[i] is not None:
            current.right = TreeNode(nodes_list[i])
            queue.append(current.right)
        i += 1
    return root

# --- Running the Test Cases ---

# Helper print formatting
def print_result(tree1_list, tree2_list):
    t1 = build_tree(tree1_list)
    t2 = build_tree(tree2_list)
    if isSameTree(t1, t2):
        print("Output: Both trees are identical")
    else:
        print("Output: Trees are not identical")


# Test Case 1: Identical Arrangement and Data
print("Test Case 1:")
print_result([1, 2, 3, 4], [1, 2, 3, 4]) 

print("\nTest Case 2:")
# Test Case 2: Different data (Node 5 instead of Node 2)
print_result([1, 2, 3, 4], [1, 5, 3, 4])