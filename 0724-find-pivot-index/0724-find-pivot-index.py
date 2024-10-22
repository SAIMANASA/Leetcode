class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        frontsum=[nums[0]]
        for i in range(1,len(nums)):
            frontsum.append(nums[i]+frontsum[i-1])
        #backsum
        backsum=[nums[len(nums)-1]]
        for i in range(len(nums)-2,-1,-1):
            backsum.append(nums[i]+backsum[(len(nums)-1)-i-1])
        backsum.reverse()
        
        for i in range(0,len(nums)):
            if frontsum[i]==backsum[i]:
                return i
        return -1


        