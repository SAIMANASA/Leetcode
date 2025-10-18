class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        l,r=0,len(nums)-1
        while(l <=r):
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            #left sorted portion
            if nums[l] <= nums[mid]:
                if target < nums[l] or nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1 
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid-1
                else:
                    l= mid +1
        
        return -1
