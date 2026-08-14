class Solution:
    def maxDifference(self, s: str) -> int:
        freq={}
        ans=0
        mini=float("inf")
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        for i in freq.values():
            if i%2!=0:
                ans=max(ans,i)
            else:
                mini=min(mini,i)
        return ans-mini
            