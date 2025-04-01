class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashransom = dict()
        for i in magazine:
            hashransom[i] = 1 + hashransom.get(i,0)
        
        for i in ransomNote:
            if i not in hashransom or hashransom [i] <=0:
                return False 
            hashransom[i] -= 1
        return True 


        """
         # Create Counter objects for the ransomNote and magazine strings
        note, mag = Counter(ransomNote), Counter(magazine)
        
        # Check if the intersection of note and mag Counter objects is equal to note Counter object
        # If it is, it means that all the letters in ransomNote can be formed using the letters in magazine
        if note & mag == note: return True
        return False


        if len(ransomNote) > len(magazine):
            return False
            
        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False

        return True
        """


        