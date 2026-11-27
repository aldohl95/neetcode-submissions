class Solution:
    def isValid(self, s: str) -> bool:
        closer = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char in closer:
                if stack and closer[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False