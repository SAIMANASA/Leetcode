class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        #brute force 
        if t == '':
            return ''
        
        res , reslen = [-1,-1], float("infinity")
       
        need= {}
        for c in t:
            need[c] = 1 + need.get(c,0) 
        for i in range(0,len(s)):
            have = {}
            for j in range(i,len(s)):
                have[s[j]] = 1 + have.get(s[j],0)
                flag = True
                for c in need:
                    if need[c] > have.get(c, 0):
                        flag = False
                        break

                if flag and (j - i + 1) < reslen:
                    reslen = j - i + 1
                    res = [i, j]
        l, r = res
        return s[l : r + 1] if reslen != float("infinity") else ""
        """
        
        if t == '':
            return ''
        
        res , reslen = [-1,-1], float("infinity")
        window , countT = {},{}
        for i in t:
            countT[i]=1+countT.get(i,0)
        have , need = 0, len(countT)
        l=0
        for r in range(0, len(s)):
            c=s[r]
            
            window[c]=1+window.get(c,0)
            if c in countT and countT[c] == window[c]:
               
                have+=1
           
            while have == need:
               

                if (r-l+1) < reslen:
                    res=[l,r]
                    reslen = r-l+1
                window[s[l]]-=1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if reslen != float("infinity") else ''
        
        