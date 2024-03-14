class Solution:
    def reverseWords(self, s: str) -> str:
        s= s.split()
        return " ".join(s[::-1])
        ###creating a deque here
        ##stringbuilder = collections.deque()
        ##start =-1
        ##i=0
        ##while(i < len(s)):
        ##    if s[i]!=' ':
         ##       start = i
        ##        while(i<len(s) and s[i]==' '):
        ##            i+=1
        ##        stringbuilder.appendleft(s[start:i])
        ##       i-=1
        ##    i+=1
        ##return "".join(stringbuilder)
        ### s = s.strip()
    ##w = []
    ##w = s.split(" ")
    ##l = []
    ##for i in w[::-1]:
    ##    if i == '':
    ##        continue
    ##    else:
    ##        l.append(i)
    ##s1 = ""
    ##s1 = " ".join(l)
    ##return s1
    ##another
    ##***return ' '.join(s.split()[::-1])​
