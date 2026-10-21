class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for n in tokens:
            if n == "+":
                stk_2 = stack.pop()
                stk_1 = stack.pop()
                new_val = int(stk_1) + int(stk_2)                
                stack.append(new_val)
            elif n == "-":
                stk_2 = stack.pop()
                stk_1 = stack.pop()
                new_val = int(stk_1) - int(stk_2)
                stack.append(new_val)
            elif n == "*":
                stk_2 = stack.pop()
                stk_1 = stack.pop()
                new_val = int(stk_1) * int(stk_2)
                stack.append(new_val)
            elif n == "/":
                stk_2 = stack.pop()
                stk_1 = stack.pop()
                new_val = int(int(stk_1) / int(stk_2))
                stack.append(new_val)
            else:
                stack.append(n)

        return int(stack[0])