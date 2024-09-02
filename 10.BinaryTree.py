class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def show(self):
        print(self.val)

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.val, end=' ')
        in_order_traversal(node.right)

def pre_order_traversal(node):
    if node:
        print(node.val, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.val, end=' ')

from collections import deque

def level_order_traversal(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

if __name__ == "__main__":
    # Creating the nodes of the tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Example usage:
    print("In-order Traversal:")
    in_order_traversal(root)
    print()  # Newline after traversal
    
    print("Pre-order Traversal:")
    pre_order_traversal(root)
    print()  # Newline after traversal

    print("Post-order Traversal:")
    post_order_traversal(root)
    print()  # Newline after traversal

    print("Level-order Traversal:")
    level_order_traversal(root)
    print()  # Newline after traversal

