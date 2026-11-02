class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = {"+", "*", '-', '/'}
        stack = []
        for ele in tokens:
            print(ele)
            print('b: ', stack)
            if ele not in operators:
                stack.append(int(ele))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if ele == "+":
                    num3 = num1 + num2
                elif ele == "-":
                    num3 = num1 - num2
                elif ele == "*":
                    num3 = num1 * num2
                elif ele == '/':
                    num3 = int(num1 / num2)
                else:
                    num3 = 0
                stack.append(num3)
            print('a: ', stack)
        return stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol = Solution()
ans = sol.evalRPN(tokens)
print(ans)