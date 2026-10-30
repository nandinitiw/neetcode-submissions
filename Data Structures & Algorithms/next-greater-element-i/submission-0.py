class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #inputs - 2 integer arrays
        #nums1 subset of nums2
        #nums2 has UNIQUE elems 
        #need to find greater element to the right of corresponding element in nums2
        # -- given integers in nums1

        
        cor_indices = []
        #find cor_index of corresponding integer in nums2, given an integer in nums1
        #create a hashmap for o(1) look up, having values of nums[2] as keys for indices
        nums2_map = {value:idx for idx,value in enumerate(nums2)}
        for i in range(len(nums1)):
            cor_indices.append(nums2_map[nums1[i]]);

        #declare array to hold all next_greater_elems
        next_greater_elems = [-1]*len(nums1)

        #search cor_index to end of nums2, returning first greater value as 
        # -- we traverse the array to the right
        for i in range(len(cor_indices)):
            start = cor_indices[i]
            for j in range(start+1, len(nums2)):
                if nums2[j]>nums1[i]:
                    next_greater_elems[i] = nums2[j]
                    break
        return next_greater_elems
        


            

