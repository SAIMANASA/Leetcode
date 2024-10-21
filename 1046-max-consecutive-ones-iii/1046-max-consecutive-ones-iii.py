#https://www.youtube.com/watch?v=4velNAJGnnM&t=402s
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_num,l=0,0
        for r,num in enumerate(nums):
            k-=1-num #or
            """
            k-=1-num means we are subtracting if it's 1 like k-1-1= 2-0  
            =remains 2 or we can write as below    
            if num=0:
                k-=1
            """
            if k<0:
                k+=1-nums[l]
                l+=1
            else:
                max_num=max(max_num,r-l+1) 
        return max_num
