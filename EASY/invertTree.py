class TreeNode:

    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


def invertBST(root):
    if not root:
        return None
    right = invert(root.right)
    left = invert(root.left)
    root.left = right
    root.right = left
    return root

#tests
#test1
sentinel = TreeNode()
curr_node = sentinel
for i in [4,2,7,1,3,6,9]:
    if i > curr_node.val:
        temp_node = TreeNode(i)
        curr_node.right = temp_node
        curr_node = curr_node.right
    else:
        temp_node = TreeNode(i)
        curr_node.left = temp_node
        curr_node = curr_node.left
ans = invertBST(sentinel.)
while sentinel:
    print(sentinel.val)
    
