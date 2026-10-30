class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #goal: replace the last n value in nums1 with nums2 elements IN PLACE
        # -- and keep the entire array sorted in non-dec order

        #ideal case: we insert new element at the correct index to keep it sorted

        #fill in elements from nums2 into the end of nums1
        #at each point, we must track greatest element of nums1 vs nums2

        i = m-1 #greatest VALID element of nums1
        j = n-1 #greatest element of nums2
        k = m+n-1 #where we are inserting new values (starting from end)

        #loop header - figure out later
        while j>=0:
            if i>=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                nums1[i] = nums2[j]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
            

            





        


        
        