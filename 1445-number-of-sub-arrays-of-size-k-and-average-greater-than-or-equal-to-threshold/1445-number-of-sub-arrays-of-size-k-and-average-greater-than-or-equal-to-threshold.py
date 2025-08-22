class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        res=0
        currsum = sum(arr[: k-1])

        for l in range(len(arr) - k +1):
            cursum+=arr[l+k-1]
            if (cursum/k > = threshold):
                res+=1
            cursum - = arr[l]
        return res
        """
        l = 0
        res = 0
        currSum = 0

        for r in range(len(arr)):
            currSum += arr[r]

            # expand Window until received size of k 
            if r - l + 1 < k:
                continue
                        
            if currSum / k >= threshold:
                res += 1

            # Shrink Window
            currSum -= arr[l]
            l += 1

        return res
        
            


        