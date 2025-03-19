class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's algorithm
        global_max = float('-inf')
        cur_sum = 0

        for num in nums:
            cur_sum += num
            global_max = max(global_max, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        
        return global_max
        