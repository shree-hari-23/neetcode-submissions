class Solution:
    def palindrome(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]

    def longestPalindrome(self, s: str) -> str:
        ans=""
        for i in range(len(s)):
            #odd length palindrome
            temp=self.palindrome(s,i,i)
            if len(temp)>len(ans):
                ans=temp
            #even length palidrome
            temp=self.palindrome(s,i,i+1)
            if len(temp)>len(ans):
                ans=temp
        return ans
        