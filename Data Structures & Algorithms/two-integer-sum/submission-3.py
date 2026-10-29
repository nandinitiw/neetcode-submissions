class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use hashmap of nums for o(1) lookup
        #map the value to the index so we can lookup index using value
        #for each iteration of nums, check if target-nums[i] in hashmap
        #also check i doesnt equal to corresponding index
        #if so, return the corresponding indices

        nums_map = {value: index for index, value in enumerate(nums)}

        for i in range(len(nums)):
            if target-nums[i] in nums_map and i != nums_map[target-nums[i]]:
                return [i, nums_map[target-nums[i]]]

        return [-1,-1]