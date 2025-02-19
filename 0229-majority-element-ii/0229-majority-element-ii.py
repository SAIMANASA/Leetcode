class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)
        ele,count=0,0
        maxtimes=0
        result=[]
        for i in nums:
            if i == ele:
                count+=1
                ele=i
           
            else:
                ele=i
                count=1
            if count > abs(len(nums)/3) and ele not in result:
                    result.append(ele)
        return result


        