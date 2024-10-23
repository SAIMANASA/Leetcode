from collections import Counter
#counter returns dictionary
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        new=Counter(arr)
        print(new)
        n1=set()
        for i in new.values():
            if i in n1:
                return False
            else:
                n1.add(i)
        return True
                
            

        