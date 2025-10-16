class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        ans = [ 1 for i in range(len(nums))]
        for i in range(0, len(nums)-1):
            ans[i+1] = prefix*nums[i]
            prefix= prefix*nums[i]
        for i in range(len(nums)-2, -1,-1):
            postfix= postfix*nums[i+1]
            ans[i] = postfix*ans[i]
          
        return ans
        

        

        