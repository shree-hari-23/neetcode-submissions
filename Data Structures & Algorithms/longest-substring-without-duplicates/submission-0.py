class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n=len(s)
        l=0
        ans=0
        dici={}
        for r in range(n):
            if s[r] in dici:
                dici[s[r]]+=1
            else:
                dici[s[r]]=1

            while dici[s[r]]>1:
                dici[s[l]]-=1
                if dici[s[r]]==0:
                    dici.pop(s[l])
                l+=1
            ans=max(ans,r-l+1)
        return ans
            