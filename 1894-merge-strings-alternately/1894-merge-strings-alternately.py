class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #merge word
        merge=''
        i=0
        if len(word1) > len(word2):
            while(i<len(word2)):
                merge+=word1[i]
                merge+=word2[i]
                i+=1
            merge+=word1[i:]
        else:
            while(i<len(word1)):
                merge+=word1[i]
                merge+=word2[i]
                i+=1
            merge+=word2[i:]
        return merge

        