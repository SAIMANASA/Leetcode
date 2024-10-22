class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        totalgain=[0]+[i for i in gain]
        for i in range(1,len(totalgain)):
        
            totalgain[i]=totalgain[i]+totalgain[i-1]
        
        return max(totalgain)
        