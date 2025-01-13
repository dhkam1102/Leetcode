class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token in operators:
                first = stack.pop()
                second = stack.pop()

                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(second - first)
                elif token == "*":
                    stack.append(second * first)
                elif token == "/":
                    stack.append(int(second / first))

            else:
                stack.append(int(token))

        return stack[-1]