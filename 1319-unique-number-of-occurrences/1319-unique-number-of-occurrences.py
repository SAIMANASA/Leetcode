from collections import Counter
#counter returns dictionary
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        new=Counter(arr)
        
        n1=set()
        for i in new.values():
            if i in n1:
                return False
            else:
                n1.add(i)
        return True
    # return True if len(set(counts.values())) == len(counts.values()) else False if used sets

    """
    freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        return len(freq) == len(set(freq.values()))
        """
                
            

        