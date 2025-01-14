class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
      
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i 

        """
         n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums) or 

        n = len(nums)
        xorr = n
        for i in range(n):
            xorr = xorr ^ i ^ nums[i]
        return xorr
        """


        