class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[count]=nums[i]
                count+=1
        return count

        """
        s = set(nums)
        nums.clear()
        for i in s:
            nums.append(i)
        nums.sort()
        return len(nums)
        """


        