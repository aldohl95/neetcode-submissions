"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        toOld = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            toOld[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = toOld[cur]
            copy.next = toOld[cur.next]
            copy.random = toOld[cur.random]
            cur = cur.next
        return toOld[head]
        
