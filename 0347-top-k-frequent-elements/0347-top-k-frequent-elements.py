import itertools
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        https://leetcode.com/problems/top-k-frequent-elements/solutions/
        1705495/python-4-ways-of-doing-same-simple-thing
        #most_common() is a built-in method provided by the Counter class 
        #in Python’s collections module. 
        
        #most_common([n]) returns a list of the n most common elements and   
        #their counts from the counter.
        count = Counter(nums)
        final = []

        for item, freq in count.most_common(k):
            final.append(item)

        return final
        """

        """
        import heapq
        from collections import defaultdict 
        class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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


        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n,0)

        for n,c in count.items():
            freq[c].append(n)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
