class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #o(1) lookup - use a hashset
        #map value to index
        nums_set = {value: index for index, value in enumerate(nums)}
        #on each iteration, check whether the difference is in the hashmap
        for i in range(len(nums)):
            #if so, check that the index is not equal to the other
            if target-nums[i] in nums_set and nums_set[target-nums[i]]!=i:
                return[i, nums_set[target-nums[i]]]

        return [-1,-1]