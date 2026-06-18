class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        nums = []
        tokens2 = []

        for i in range(len(tokens)):
            tokens2.append(tokens.pop())
        print(tokens2)

        while len(tokens2) > 0:
            print
            print(nums)
            try:
                nums.append(int(tokens2[len(tokens2)-1]))
                tokens2.pop()
                #basically this is still popping the value even if it isnt an integer in the process of trying
                #so need to first see if it works, then pop that value
            except:
                a = int(nums.pop())
                b = int(nums.pop())
                nums.append(self.evaluate(b, a, tokens2.pop()))
        
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


        