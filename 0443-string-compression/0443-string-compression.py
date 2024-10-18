class Solution:
    def compress(self, chars: List[str]) -> int:
        index=0
        i=0
        if len(chars)==1:
            return 1
        while(i<len(chars)):
            j=i
            while(j<len(chars) and chars[i]==chars[j]):
                j+=1
            
            chars[index]=chars[i]
            if(j-i > 1):
               count=j-i
               
               for digit in str(count):
                    index+=1
                    chars[index] = digit
                    
            
            index+=1


            i=j
        return index
       



            

        