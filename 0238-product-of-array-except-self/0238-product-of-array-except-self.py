class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans=[0 for i in nums]
        ###prefix and postfix multiplication , doesn't need 2 arrays for prefix and postfix
        prefix=1
        postfix=1
        ans[0]=1
        ##prefix multiplication into the ans
        for i in range(0,len(nums)-1):
            ans[i+1]=prefix*nums[i]
            prefix=prefix*nums[i]
        print(ans)
        ##postfix multiplication into ans
        for i in range(len(nums)-2,-1,-1):
            postfix=postfix*nums[i+1]
            ans[i]=postfix*ans[i]
        return ans
        