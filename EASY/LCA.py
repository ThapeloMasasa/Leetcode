# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

class TreeNode:

    def __init__(self):
        self.val = 0
        self.right = None
        self.left = None

def lowestCommonAncenstor(root, p, q):
    p_val = p.val
    q_val = q.val
    node = root
    while node:
        parent_val = node.val
        if p_val >  parent_val and q_val > parent_val:
            node = node.right
        elif p_val <  parent_val and q_val < parent_val:
            node = node.left
        else:
            return node
    


