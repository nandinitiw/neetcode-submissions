class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lo = 0 
        hi = len(nums)

        while lo<hi:
            mid = ((hi+lo)//2) #int division
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                lo = mid + 1
            if nums[mid]>target:
                hi = mid

        return -1
