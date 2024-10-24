class Solution:
    def removeStars(self, s: str) -> str:
        result=[]
        for i in s:
            if i =='*':
                result.pop()
            else:
                result.append(i)
        print(result)
        if len(s)==0 or len(result)==0:
            return ""
        else:
            Newstr=''
            for i in result:
                Newstr+=str(i)
        return Newstr

        