class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        counts = {}
        unique_elems = set(nums) #has the number of UNIQUE elements in nums
        for i in range(len(unique_elems)):
            cur_elem = nums[0]
            cur_freq = 0
            while(cur_elem in nums):
                cur_freq += 1
                counts[cur_elem]= cur_freq
                nums = nums[1:len(nums)]


                #avoid deletion, is there a way?? put in in hash set SEEN. ooh.

                #if the element is in seen, increase freq and 
            print(cur_freq)

        ans = []
        for i in range(k):
            ans.append(max(counts, key=lambda key: counts[key]))
            del counts[max(counts, key=lambda key: counts[key])]
        
        return ans