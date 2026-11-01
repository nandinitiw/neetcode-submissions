class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for day, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                j=stack.pop()
                res[j] = day-j
            stack.append(day)
        
        return res


        
        


        


        

