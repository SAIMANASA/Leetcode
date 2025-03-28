class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        left = 0 
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

        """

        s=s.lower()
        s1=''
        for i in s:
            if i.isalpha() or i.isnumeric():
                s1+=i
        
        s2="".join(reversed(s1))
       
        if s1==(s2):
            return True
        else:
            return False
        """