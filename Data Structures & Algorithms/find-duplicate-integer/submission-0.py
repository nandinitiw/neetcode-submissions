class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #can use tortoise and hare method to check
        #for cycles (points to same value)
        #comparing POINTERS!!
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] #skips ahead two pointers
            if slow==fast: #compares pointers
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow==slow2:
                break
        
        return slow
        