# Given a binary tree, determine if it is height-balanced



def balancedBST(root):
    if not root:
        return True
    right_depth = self.depth(root.right)
    left_depth = self.depth(root.left)

    if abs(right_depth - left_depth) > 1:
        return False
    else:
        return self.balancedBST(root.left) and self.balancedBST(root.right)

    

def depth(node):
    if not root:
        return 0
    else:
        return 1 + max(self.depth(node.right), self.depth(node.left))