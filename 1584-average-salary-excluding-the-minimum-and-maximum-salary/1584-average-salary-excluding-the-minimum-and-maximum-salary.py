class Solution:
    def average(self, salary: List[int]) -> float:
        salary1=sorted(salary) ##salary.sort()
       
        count=0
        sum1=0
        for i in range(1,len(salary)-1):
            count+=1
            sum1+=salary1[i]
        return (sum1/count)


"""
class Solution(object):
    def average(self, salary):
        return float(sum(sorted(salary)[1:-1]))/float(len(salary)-2)
        or
                 salary.remove(max(salary))
        salary.remove(min(salary))
        return sum(salary)/len(salary)
        or  
      def average(self, salary: List[int]) -> float:
        salary.sort()
        return (sum(salary)-salary[0]-salary[-1])/(len(salary)-2) 
        
    """

    
        
