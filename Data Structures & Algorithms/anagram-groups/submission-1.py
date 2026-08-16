class Solution:
    def sortstring(self,s):
        s=list(s)
        s.sort()
        return "".join(s)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dici={}
        for s in strs:
            key=self.sortstring(s)
            if key in dici:
                dici[key].append(s)
            else:
                dici[key]=[s]
        return list(dici.values())
        