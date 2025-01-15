class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return int(min(len(candyType)/2,len(set(candyType))))

        """
         maxi=len(candyType)//2
        d={}
        for i in candyType:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=len(d)
        return min(l,maxi) """
        