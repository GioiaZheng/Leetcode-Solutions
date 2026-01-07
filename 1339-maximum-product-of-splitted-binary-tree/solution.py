from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        subtree_sums = []

        # First DFS: compute all subtree sums
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            subtree_sums.append(s)
            return s

        total_sum = dfs(root)

        # Try splitting at every subtree
        max_product = 0
        for s in subtree_sums:
            max_product = max(max_product, s * (total_sum - s))

        return max_product % MOD
