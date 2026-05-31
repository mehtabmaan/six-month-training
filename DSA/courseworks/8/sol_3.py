class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkSubtreeSum(root: TreeNode, target_sum: int) -> bool:
    # We use a list containing a boolean to act as a mutable global flag inside helper
    found = [False]
    
    def calculate_subtree_sum(node):
        if not node:
            return 0
        
        # 1. Recursively find the sum of left and right subtrees
        left_sum = calculate_subtree_sum(node.left)
        right_sum = calculate_subtree_sum(node.right)
        
        # 2. Total sum of the subtree rooted at the current node
        current_sum = node.val + left_sum + right_sum
        
        # 3. Check if this subtree's sum equals the target sum
        if current_sum == target_sum:
            found[0] = True
            
        return current_sum

    # Start the post-order traversal
    calculate_subtree_sum(root)
    return found[0]


# --- Helper function to build the tree from level order format ---
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

# The tree representation from your examples: [1, 3, 6, 5, 9, 8]
# Note: Node 6's right child is missing, so we use None for structural accuracy
tree_nodes = [1, 3, 6, 5, 9, 8, None]
tree_root = build_tree(tree_nodes)

# Test Case 1: Target sum = 17
sum1 = 17
result1 = "“Yes”" if checkSubtreeSum(tree_root, sum1) else "“No”"
print(f"Input Sum: {sum1} -> Output: {result1}") 
# Explanation: Subtree rooted at 3 has nodes {3, 5, 9} -> 3 + 5 + 9 = 17

# Test Case 2: Target sum = 11
sum2 = 11
result2 = "“Yes”" if checkSubtreeSum(tree_root, sum2) else "“No”"
print(f"Input Sum: {sum2} -> Output: {result2}")