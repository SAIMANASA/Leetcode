class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueele= {}
        l=0
        count =0
        
        for r in range(len(s)):

            if s[r] in uniqueele and uniqueele[s[r]] >= l:
                
                l = uniqueele[s[r]]+1
                
                
            
            uniqueele[s[r]] = r
            count = max(count ,r-l+1)
        return count 
                
        
            

        