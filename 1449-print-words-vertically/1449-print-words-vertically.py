class Solution:
    def printVertically(self, s: str) -> List[str]:
        wordlist=s.split()
        maxword=0
        total=[]
        
        for i in wordlist:
            maxword=max(len(i),maxword)
            
        for i in range(maxword):
            emptystring = ''
            for word in wordlist:
                emptystring += " " if i > len(word)-1 else word[i]
                
            total.append(emptystring.rstrip())
        return total 

        """
         s = s.split(" ")
        maximum : int = max([len(word) for word in s])
        
        total : list[str] = []
        for index in range(maximum):
            this_sequence : str = ""

            for word in s:
                this_sequence += " " if index > len(word) - 1 else word[index]

            total.append(this_sequence.rstrip())
        """ 
        """
        a, b, words = [], [], s.split()
        max_length = len(max(words, key=len))
        for i in words:
            if len(i) < max_length:
                i =  i + " " * (max_length - len(i)) 
            a.append(i)
        for i in zip(*a):
            b.append(''.join(i).rstrip())
        return b
        """ 

        """
        from itertools import zip_longest
        from typing import Iterable


        class Solution:
            def printVertically(self, s: str) -> Iterable[str]:
            return map(str.rstrip, map(''.join, zip_longest(*s.split(), fillvalue=' ')))
            or 
            return [''.join(a).rstrip() for a in itertools.zip_longest(*s.split(), fillvalue=' ')]
        """ 
            



        
        