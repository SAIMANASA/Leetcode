class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize a dictionary to store character counts
        count = {}

        # Count characters in string t
        for c in t:
            count[c] = count.get(c, 0) + 1

        # Subtract counts for characters in string s
        for c in s:
            count[c] -= 1
            if count[c] == 0:
                del count[c]

        # The remaining character in the dictionary is the difference
        return list(count.keys())[0]


        """
        res = 0
        
        # XOR all characters in s and t
        for char in s + t:
            res ^= ord(char)
        
        # Convert the XOR result back to character
        return chr(res)



        or   hASHING 
         for c in t:
            if t.count(c) > s.count(c):
                return(c)
        """


        
        