import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        res = r # to initiate max so that we can compare to get min , since max it can eat  

        while(l <= r):
            k = (l+r)//2
            total_hours = 0
            for i in piles:
                total_hours += math.ceil(i / k) 
            if total_hours <=h:
                res = min(res,k)
                r = k-1
            else:
                l = k + 1
        return res

        