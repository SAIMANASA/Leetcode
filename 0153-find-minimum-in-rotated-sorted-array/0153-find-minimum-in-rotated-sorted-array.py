class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) -1
        res = nums[0]
        while(l<=r):
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break 
            mid = (l+r)//2
            res = min(res,nums[mid])

            if nums[mid] >= nums[r]:
                l = mid+1
            else:
                r = mid -1


        return res
            

        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        
        return nums[left]
        """
        