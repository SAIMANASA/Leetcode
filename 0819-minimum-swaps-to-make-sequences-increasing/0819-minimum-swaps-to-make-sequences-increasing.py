class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        #https://www.youtube.com/watch?v=mLTF2UXkd2o&t=358s
        n1, s1 = 0, 1
        for i in range(1, len(nums1)):
            n2 = s2 = float("inf")
            if nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
                n2 = min(n2, n1)
                s2 = min(s2, s1 + 1)
            if nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]:
                n2 = min(n2, s1)
                s2 = min(s2, n1 + 1)

            n1, s1 = n2, s2

        return min(n1, s1)
        