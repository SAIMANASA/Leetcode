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
                    
                
            
                
        