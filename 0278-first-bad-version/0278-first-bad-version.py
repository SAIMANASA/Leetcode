# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        small = 1
        large = n
        if n == 1:
            return n 


        while small < large :

            mid = small + (large-small)//2
            if isBadVersion(mid) is False:

                small=mid+1  # The first bad version must be after mid.

            else:

                large = mid   # The first bad version could be mid or before.


        return small # At the end, first will be the first bad version.