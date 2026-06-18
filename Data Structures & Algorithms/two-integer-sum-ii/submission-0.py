class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #increasing order, 
        done = False

        start = 0
        end = len(numbers)-1

        while not done:
            sum = numbers[start]+numbers[end]
            if(sum<target):
                start += 1
            if(sum>target):
                end -= 1
            if(sum==target):
                done = True
        
        return [start+1, end+1]