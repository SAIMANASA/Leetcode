class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        if len(s) != len(t):
            return False
        s=sorted(s)
        t=sorted(t)
        if s==t:
            return True
        return False
        # return Counter(s) == Counter(t)
        