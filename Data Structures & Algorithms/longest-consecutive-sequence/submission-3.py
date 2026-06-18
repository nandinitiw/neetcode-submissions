class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #want to check if successor exists in the hash set
        #if so, remove and increase count

        numset = set(nums)
        longest = 0

        for i in range(len(nums)):
            count = 1
            while nums[i]+1 in numset:
                count += 1
                nums[i] = nums[i]+1
            longest = max(count, longest)
            
        return longest




        