Here's an explanation of the approach used in this code:

s.split(): The split() method is used to split the input string s into a list of words. By default, it splits the string at spaces (whitespace characters), effectively separating the words. For example, "Hello World" becomes ["Hello", "World"].

s[::-1]: After splitting the string into words, the list of words is reversed using slicing with [::-1]. This reverses the order of elements in the list, effectively reversing the order of words. For example, ["Hello", "World"] becomes ["World", "Hello"].

" ".join(...): Finally, the reversed list of words is joined back into a single string using the join() method. This method joins the elements of the list using a space as a separator, effectively creating a string with the reversed word order. For example, ["World", "Hello"] becomes "World Hello".

Complexity
Time complexity: O(n + m)
Space complexity: O(n + m)
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
