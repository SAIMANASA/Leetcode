class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for i in range(round((num+2)**0.5),0,-1):
            if (num+1)%i == 0:
                return [i,(num+1)//i]
            if (num+2)%i == 0:
                return [i,(num+2)//i]
        

        
        
        """
        def find_divisors(x):
            val = int(math.sqrt(x)) 

            for i in range(val,0,-1):
                if x%i == 0:
                    return [i,x//i]

            return []

        res = [find_divisors(num+1)] + [find_divisors(num+2)]
        print(res)

        res.sort(key = lambda x: abs(x[0]-x[1]))
        #above statement for ex: 123 gets [[4,31],[5,25]] which 
        #when lambda 4-31 =27 and 5-25 = 20 , less difference is 20 
        #so, gives [5,25]

        return res[0]
        """
        

        