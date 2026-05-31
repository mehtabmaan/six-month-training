class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    # Base case: If the node is empty, depth is 0
    if not root:
        return 0
    
    # Recursively find the depth of left and right subtrees
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    # The depth of the current node is 1 plus the max of its subtrees
    return max(left_depth, right_depth) + 1

# --- Helper function to build the tree from the test case format (Level Order) ---
def build_tree_from_list(nodes_list):
    if not nodes_list:
        return None
    
    root = TreeNode(nodes_list[0])
    queue = [root]
    i = 1
    
    while queue and i < len(nodes_list):
        current = queue.pop(0)
        
        # Assign left child
        if i < len(nodes_list) and nodes_list[i] is not None:
            current.left = TreeNode(nodes_list[i])
            queue.append(current.left)
        i += 1
        
        # Assign right child
        if i < len(nodes_list) and nodes_list[i] is not None:
            current.right = TreeNode(nodes_list[i])
            queue.append(current.right)
        i += 1
        
    return root

# --- Running the Test Cases ---

# Test Case 1
test_case_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tree_1 = build_tree_from_list(test_case_1)
print(f"Maximum depth of tree is {maxDepth(tree_1)}")  # Output: 4

# Test Case 2
test_case_2 = [1, 2, 3, 4, 5]
tree_2 = build_tree_from_list(test_case_2)
print(f"Maximum depth of tree is {maxDepth(tree_2)}")  # Output: 3