class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #unique elements need to be first in the array
        #anything can come afterwards

        #initialize return value
        unique_elems = 0
        next_unique_idx = 0
        #initialize hash set
        elems = set()
        #iterate through nums 
        for i in range(len(nums)):
        #on each iteration, check if nums[i] is in the hash set
        #if not, add to hash set and increment return value
            if nums[i] not in elems:
                elems.add(nums[i])
                unique_elems+=1
                nums[next_unique_idx]=nums[i]
                next_unique_idx += 1

        return unique_elems


