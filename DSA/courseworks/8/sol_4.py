class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSumTree(root: TreeNode) -> bool:
    
    # Helper function returns a tuple: (is_valid_sum_tree, total_sum_of_subtree)
    def check_tree(node):
        # Base Case 1: Empty node is a SumTree, and its sum is 0
        if not node:
            return True, 0
        
        # Base Case 2: A leaf node is a SumTree, and its sum is its own value
        if not node.left and not node.right:
            return True, node.val
        
        # Recursively check the left and right subtrees
        is_left_valid, left_sum = check_tree(node.left)
        is_right_valid, right_sum = check_tree(node.right)
        
        # Rule condition check:
        # Current node is a SumTree ONLY IF left subtree is valid, 
        # right subtree is valid, AND current value equals left sum + right sum.
        is_current_valid = is_left_valid and is_right_valid and (node.val == left_sum + right_sum)
        
        # Total sum returned up the stack is: Node value + Left subtree sum + Right subtree sum
        total_sum = node.val + left_sum + right_sum
        
        return is_current_valid, total_sum

    # Return only the boolean flag from our helper function
    is_valid, _ = check_tree(root)
    return is_valid


# --- Helper function to build the tree from Level Order format ---
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

# Test Case 1: Valid SumTree
# Note: Node 3 has no left child, so we pass None to keep structural alignment [..., 3, 4, 6, None, 3]
tc1_nodes = [26, 10, 3, 4, 6, None, 3]
tree1 = build_tree(tc1_nodes)
print("Test Case 1:")
if isSumTree(tree1):
    print("Output: The given tree is a SumTree")
else:
    print("Output: The given tree is not a SumTree")

print("-" * 35)

# Test Case 2: Invalid SumTree
tc2_nodes = [1, 3, 6, 5, 9, 8, None]
tree2 = build_tree(tc2_nodes)
print("Test Case 2:")
if isSumTree(tree2):
    print("Output: The given tree is a SumTree")
else:
    print("Output: The given tree is not a SumTree")