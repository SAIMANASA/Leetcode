class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        import sys
        
        #tc - o(n) -- kadane algo
        """
        currmax= nums[0]
        currmin = nums[0]
        maxprod = nums[0]
        for i in range(1,len(nums)) :
            currmax = max(nums[i],nums[i]*currmax,nums[i]*currmin)
            currmin  = min(nums[i],nums[i]*currmax,nums[i]*currmin)
            maxprod = max(maxprod,currmax)
        return maxprod

        """

        #maxprod = -sys.maxsize
        maxprod = float('-inf')     
        lefttoright = 1
        righttoleft = 1
        for i in range(0,len(nums)):
            if lefttoright == 0:
                lefttoright = 1
            if  righttoleft == 0:
                righttoleft = 1
            lefttoright *=nums[i]
            j=len(nums)-i-1
            righttoleft*=nums[j]
            maxprod=max(lefttoright,righttoleft,maxprod)
        return maxprod

