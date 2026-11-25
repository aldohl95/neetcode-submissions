class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currString = ""
        number = 0

        for i in range(len(s)):
            if s[i].isdigit():
                number = number * 10 + int(s[i])
            elif s[i] == "[":
                stack.append([number, currString])
                currString = ""
                number = 0
            elif s[i] == "]":
                count, string = stack.pop()
                currString = string + count * currString
            else:
                currString += s[i]
        return currString 