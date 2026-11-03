class Solution:
    def isValid(self, s: str) -> bool:
        pair = {']':'[', '}':'{',')':'('}
        stack = []

        for sym in s:
            if len(stack) == 0 and sym in pair:
                return False
            if len(stack) > 0 and sym in pair:
                if stack[-1] == pair[sym]:
                    stack.pop()
                else:
                    return False
            if sym not in pair:
                stack.append(sym)
        if len(stack) == 0:
            return True
        return False
