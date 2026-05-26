from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Returns a tuple: (deepest_depth, subtree_root)
        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0, None

            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)

            if left_depth > right_depth:
                return left_depth + 1, left_node
            elif right_depth > left_depth:
                return right_depth + 1, right_node
            else:
                # Both sides have the same deepest depth
                # Current node is the LCA of deepest nodes
                return left_depth + 1, node

        return dfs(root)[1]
