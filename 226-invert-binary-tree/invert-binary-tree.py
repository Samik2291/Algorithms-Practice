# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root:
            self.invert(root)
        return root

    def invert(self, root):
        try:
            root.right, root.left = root.left, root.right
            self.invert(root.right)
            self.invert(root.left)
        except:
            try:
                root.left, root.right = root.right, None
                self.invert(root.left)
            except:
                try:
                    root.left, root.right = None, root.left
                    self.invert(root.left)
                except:
                    pass