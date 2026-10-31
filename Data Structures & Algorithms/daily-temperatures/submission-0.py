class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #index of the next bigger value in the array

        res = [0]*len(temperatures)
        #on each iteration, start at i and traverse array o(n^2)
        
        #implement a stack, keeping track of indices that need next higher temp
        stack = []
        for day, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j=stack.pop()
                res[j] = day-j
            #adds each index needing to be searched
            stack.append(day)

        return res
                
        
        


        


        

