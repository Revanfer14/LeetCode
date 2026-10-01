class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        if len(s) % 2 != 0:
            return False

        stack = []

        dictio = {")": "(", "]": "[", "}": "{"}

        for st in s:
            if st == "(" or st == "[" or st == "{":
                stack.append(st)
            else:
                if st in dictio and stack and dictio[st] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(st)

        if stack:
            return False
        else:
            return True
