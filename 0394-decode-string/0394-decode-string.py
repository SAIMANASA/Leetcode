#https://youtu.be/qB0zZpBJlh8
class Solution:
    def decodeString(self, s: str) -> str:
        res=[]
        
        for i in s:
            
            if i==']':
                restring=''
               
                while res[-1]!='[':
                    restring=str(res.pop())+restring
                res.pop()
                k=''
                while res and res[-1].isdigit():
                    k=res.pop()+k
                res.append(int(k)*restring)
                
            else:
                res.append(i)
        return "".join(res)

