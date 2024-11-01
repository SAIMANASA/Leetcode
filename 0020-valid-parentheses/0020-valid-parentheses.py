#https://www.youtube.com/watch?v=WTzjTskDFMg&t=622s
class Solution:
    def isValid(self, s: str) -> bool:
        stck=[]
        closeToOpen={")":"(","]":"[","}":"{"}
        if len(s)==1:
            return False
        for i in s:
            
            if i in closeToOpen:
                if stck and stck[-1]==closeToOpen[i]:
                    stck.pop()
                else:
                    return False
              
               
            else:
               
                stck.append(i)
        return True if not stck else False
            