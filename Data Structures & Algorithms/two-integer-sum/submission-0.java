class Solution {
    public int[] twoSum(int[] nums, int target) {
        //one pair of indices that satisfy nums[i]+nums[j]==target
        //iterate thru array once
        //for each iteration, add element to hash set,
        //AND check if that element

        //
        // need the index of the other element in the arr 


        //iterate, while we add to the hash set:
        //check if the other part in hash set, if not, 


        int[] ans = new int[2];
        //this allows you to get the index!!
        Map<Integer, Integer> numbers = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            numbers.put(nums[i], i);
        }
        for(int i=0; i<nums.length; i++){
            if(numbers.containsKey(target-nums[i]) && numbers.get(target-nums[i]) != i){
                ans[0]=i;
                ans[1]=numbers.get(target-nums[i]);
                return ans;
            }
        }
        
        return new int[0];
    }
}
