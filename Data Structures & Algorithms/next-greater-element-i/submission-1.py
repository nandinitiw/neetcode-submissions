class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #inputs - 2 integer arrays
        #nums1 subset of nums2
        #nums2 has UNIQUE elems 
        #need to find FIRST greater element to the right of corresponding element in nums2
        # -- given integers in nums1

        stack = []
        #map value in nums2 to nge in num2
        res_map = {value:-1 for index, value in enumerate(nums2)}
        #create stack to keep track of indices for which we need to find nge
        for idx, value in enumerate(nums2):
            while stack and nums2[idx]>nums2[stack[-1]]:
                j = stack.pop()
                res_map[nums2[j]] = nums2[idx]
            
            stack.append(idx)

        #now we have an array with next greatest value in nums2 for each value
        #need this now to be in the ORDER of the original values in nums1
        res = []
        for i in range(len(nums1)):
            res.append(res_map[nums1[i]])

        return res
        


            

