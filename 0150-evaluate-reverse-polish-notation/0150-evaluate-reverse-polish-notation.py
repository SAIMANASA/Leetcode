class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stck =[]
        for i in tokens:
            if i == '+':
                stck.append(stck.pop()+stck.pop())
            elif i == '-':
                a,b = stck.pop(),stck.pop()
                stck.append(b - a)
            elif i == '*':
                stck.append(stck.pop()*stck.pop())
            elif i == '/':
                a,b = stck.pop(),stck.pop()
                stck.append(int(b/a))
            else:
                stck.append(int(i))   
        return stck[0]     