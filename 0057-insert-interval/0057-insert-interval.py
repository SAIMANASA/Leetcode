class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        """
        #bruteforce
        intervals.append(newInterval)
        intervals.sort()

        res = [intervals[0]]

        for i in range(1,len(intervals)):
            if res[-1][1] >=intervals[i][0]:
                res[-1][1] = max(res[-1][1],intervals[i][1])
            else:
                res.append(intervals[i])
        return res
        """

        res= []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            else:
                newInterval = (min(newInterval[0],intervals[i][0]),
                max(newInterval[1],intervals[i][1]))
        
        res.append(newInterval)
        return res




        