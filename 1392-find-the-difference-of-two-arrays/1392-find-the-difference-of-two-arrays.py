class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result=[]
        first1=[]
        for i in nums1:
            if i not in nums2  and i not in first1:
                first1.append(i)
        result.append(first1)
        second=[]
        for i in nums2:
            if i not in nums1 and i not in second:
                second.append(i)
        result.append(second)
        return result
        