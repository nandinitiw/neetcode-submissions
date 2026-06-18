class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]

'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        nums = []
        while len(tokens) > 0:
            print
            print(nums)
            try:
                nums.append(int(tokens[0]))
                del tokens[0]
            except:
                a = int(nums.pop())
                b = int(nums.pop())
                nums.append(self.evaluate(b, a, tokens[0]))
                del tokens[0]
        
        return nums[0]
    


    def evaluate(self, a: int, b: int, op: str) -> int:
        if(op=="+"):
            return a+b
        if(op=="-"):
            return a-b
        if(op=="*"):
            return a*b
        if(op=="/" and b!=0):
            return int(a/b)
        return 0

'''
        