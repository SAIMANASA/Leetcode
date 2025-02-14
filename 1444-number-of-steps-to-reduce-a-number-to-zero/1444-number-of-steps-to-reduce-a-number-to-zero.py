class Solution:
    def numberOfSteps(self, num: int) -> int:
        #https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/solutions/6397373/two-solutions-looping-integer-operations-bitwise-operation
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
    The bit_length() function in Python is used to determine the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros. It effectively calculates the length of the binary representation of an integer.

There is also the Python Bin function. The bin() function in Python converts an integer to its binary string representation

    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return num.bit_length() - 1 + num.bit_count()
          or return num.bit_length() + bin(num).count('1') - 1
    """


        