class Solution:
    def minimumLength(self, s: str) -> int:
        l=0
        r=len(s)-1
        while(l<r) and s[l]==s[r]: #breaks when s[l]!=s[r]
            temp=s[l]
            while(l<=r) and s[l]==temp:#breaks when s[l]!=s[l+1]
                l+=1
            while(l<=r) and s[r]==temp:#breaks when s[r]!=s[r-1]
                r-=1
        return (r-l+1)
    
    """
    while len(s) > 1 and s[0] == s[-1]:
            s = s.strip(s[0])
        return len(s) """