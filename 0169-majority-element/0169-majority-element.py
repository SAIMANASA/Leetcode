class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majtable=dict()
        count=abs(len(nums)/2)
        for i in nums:
            if i in majtable:
                majtable[i]+=1
               
            else:
                majtable[i]=1
            if count < majtable[i]:
                count=majtable[i]
                result=i
        return result

        """
          nums.sort()
        n = len(nums)
        return nums[n//2]
    

       #moores voting algorithm
    
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
        """