class Solution:
    def checkString(self, s: str) -> bool:
        a=0
        b=0
        for i in s: 
            if i=='a' and b>0:
                return False
            elif i=='a':
                a+=1
            else:
                b+=1
        return True