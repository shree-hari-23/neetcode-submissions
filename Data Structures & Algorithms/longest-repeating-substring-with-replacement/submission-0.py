class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        l=0
        dici={}
        maxfreq=0
        maxwindow=0
        for r in range(n):
            if s[r] in dici:
                dici[s[r]]+=1
            else:
                dici[s[r]]=1
            maxfreq=max(maxfreq,dici[s[r]])
            window=r-l+1
            while window-maxfreq>k:
                dici[s[l]]-=1
                l+=1
                window=r-l+1
            maxwindow=max(window,maxwindow)
        return maxwindow