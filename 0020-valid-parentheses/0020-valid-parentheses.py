class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        dic = {"}": "{", "]": "[", ")": "("}
        stack = []

        for i in s:
            if i in dic.values():
                stack.append(i)
            else:
                if i in dic and stack and stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        else:
            return True