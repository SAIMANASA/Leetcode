import sys
max=-sys.maxsize

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if len(arr)==1:
            return True
        if len(arr)==2:
            if arr[0]==arr[1]:
                return True
            else:
                return False
            
        unique=[]
        count=1
        arr.sort()
        for i in range(0,len(arr)-1):
            if arr[i]==arr[i+1]:
                count+=1
            else:
                if count not in unique:
                    unique.append(count)
                    count=1
                else:
                    return False
        if count not in unique:
            return True
        else:
            return False


other methods:
-----------------
 memo = []
        for i in Counter(arr).values():

            if i in memo: return False
            else:   memo.append(i)

        return True

----------------------

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        return len(set(count := Counter(arr).values())) == len(count)

---------------------------
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        memo = []
        for i in set(arr):
            i = arr.count(i)
            if i in memo: return False
            else:   memo.append(i)

        return True
                    
                
            
                
        
