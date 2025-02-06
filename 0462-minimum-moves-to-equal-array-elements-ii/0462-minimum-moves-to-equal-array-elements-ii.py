class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # return (m:=int(median(a)),sum(abs(v-m) for v in a))[1]
        # return (m:=int(median(a)))*0+sum(abs(v-m) for v in a)
        #  return sum(map(abs,(map(int(median(a)).__sub__,a))))
        nums.sort()
        count = 0
        median = nums[len(nums) // 2]
        #  return sum([abs(median - x) for x in nums])
        for num in nums:
            count += abs(median - num)

        return count
        
        