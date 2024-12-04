class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i=0
        j=0
        result=""
       
        for i in range(0,len(s)):
            if j != len(spaces) and i == spaces[j]:
                result+=' '
                result+=s[i]
                j+=1
            else:
                result+=s[i]
        
        return result
