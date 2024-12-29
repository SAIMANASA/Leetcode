class Solution:
    def average(self, salary: List[int]) -> float:
        salary1=sorted(salary) ##salary.sort()
       
        count=0
        sum1=0
        for i in range(1,len(salary)-1):
            count+=1
            sum1+=salary1[i]
        return (sum1/count)

    
        