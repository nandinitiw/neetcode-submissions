class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #want to check if successor exists in the hash set
        #if so, remove and increase count
        if(len(nums)==0):
            return 0
            
        numset = set()
        for i in range(len(nums)):
            numset.add(nums[i])
        print(numset)
        
        counts = set()
        for i in range(len(nums)):
            count = 1
            while nums[i]+1 in numset:
                count += 1
                nums[i] = nums[i]+1
            counts.add(count)
            

        #check the relative counts, find max
        return max(counts)




        