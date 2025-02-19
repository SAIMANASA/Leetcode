class Solution:
    def thousandSeparator(self, n: int) -> str:
        count=0
        n=str(n)
        result=''
        #   n=n[::-1]
        #res = '.'.join(n[i:i + 3] for i in range(0, len(n), 3))
        if len(n)<=3:
            return n
        for i in n[::-1]:
            
            count+=1
            if count==4:
                result+='.'
                result+=i
               
                count=1
            else:
                result+=i
        return result[::-1]


        