#import heapq
from collections import defaultdict, Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        counts = defaultdict(int)
        for n in nums:
            counts[n]+=1
        #minheap 
        heap=[]
        for key, val in counts.items():
            heapq.heappush(heap,(val,key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [key for (val,key) in heap]
        """

        count = Counter(nums) 

        freq = [[] for i in range(len(nums)+1)]

        for key,value in count.items():
            freq[value].append(key)

        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
       

        