class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs)
        largest = max(strs)

        for i in range(len(smallest)):
            if smallest[i] != largest[i]:
               return smallest[:i]

        return smallest
