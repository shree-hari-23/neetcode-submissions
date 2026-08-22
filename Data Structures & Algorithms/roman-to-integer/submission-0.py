class Solution:
    def romanToInt(self, s: str) -> int:
         dici={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
         sum=0
         for i in range(len(s)):
            if i+1<len(s) and dici[s[i]]<dici[s[i+1]]:
                sum-=dici[s[i]]
            else:
                sum+=dici[s[i]]
         return sum

        