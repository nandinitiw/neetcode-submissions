class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        zero_count = 0
        base=1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count+=1
            else:
                base=base*nums[i]
            print(base)

        #case 1: current val is 0 and another 0 exists -> that value is 0 DONE
        #case 2: current val is 0 and no other 0s exist -> value = base DONE
        #case 3: current val isnt 0 and another 0 exists -> that value is 0 DONE
        #case 4: current val isnt 0 and no other 0 exist -> value is base/val DONE
        
        for i in range(len(nums)):
            if(nums[i]==0 and zero_count>1) or (nums[i]!=0 and zero_count>0):
                ans.append(0)
            elif(zero_count==0 and nums[i]!=0):
                ans.append(int(base/nums[i]))
            elif(zero_count==1 and nums[i]==0):
                ans.append(base)
        
        return ans
            
            


        