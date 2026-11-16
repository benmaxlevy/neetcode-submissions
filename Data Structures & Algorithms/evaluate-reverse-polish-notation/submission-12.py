class Solution:
    def __operate(self, num1, num2, operator):
        if operator == '*':
            return num1 * num2
        elif operator == '/':
            return int(num1 / num2)
        elif operator == '-':
            return num1 - num2
        else:
            return num1 + num2
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for i,t in enumerate(tokens):
            if t not in ['+', '-', '*', '/']:
                stack.append(t)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                stack.append(self.__operate(num1, num2, t))
        return stack[-1]

                