class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosum=dict()
        for i in range(0,len(nums)):
           
            if  target-nums[i] in twosum:
                return(twosum[target-nums[i]],i)
        
            twosum[nums[i]]=i

        