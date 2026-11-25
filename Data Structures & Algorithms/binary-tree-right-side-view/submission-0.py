# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        que = deque()
        res = []
        que.append(root)
        if not que:
            return []
        while que:
            qlen = len(que)
            stack = []
            for i in range(qlen):
                node = que.popleft()
                if node:
                    que.append(node.left)
                    que.append(node.right)
                    stack.append(node.val)
            if stack:
                res.append(stack.pop())
        return res
                
                

