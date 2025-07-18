class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #idealogy : create a hashset for the value in str and search through 
        #sorted value and add to dict
        
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
        
        return list(ans.values())
        
        """
        
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        
        return list(ans.values())

        """
        