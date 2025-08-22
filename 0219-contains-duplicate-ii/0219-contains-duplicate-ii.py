class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums1=dict()
        for i in range(0,len(nums)):
            if nums[i] in nums1:
                k1 = abs(i-nums1[nums[i]])
               
                nums1[nums[i]]=i

                if k1 <= k:
                    
                    return True
                    
            else:
                nums1[nums[i]]=i
        return False

        