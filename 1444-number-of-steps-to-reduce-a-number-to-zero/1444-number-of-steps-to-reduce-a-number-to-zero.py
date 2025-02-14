class Solution:
    def numberOfSteps(self, num: int) -> int:
        """
         count=0
        while(num!=0):
            if (num%2==0):
                num=num//2
                count+=1
            else:
                num-=1
                count+=1
        return count
        """
        count=0
        while(num!=0):
            if (num&1==0):
                num=num//2
                count+=1
            else:
                num-=1
                count+=1
        return count
    """
        class Solution:
    """
        #Time:   O(log(n))
        #Memory: O(log(n))
    """

    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + self.numberOfSteps(num - 1 if num & 1 else num >> 1)
    """
    """
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return num.bit_length() - 1 + num.bit_count()
          or return num.bit_length() + bin(num).count('1') - 1
    """


        