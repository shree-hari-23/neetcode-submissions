class Solution:
    def isSubsequence(self, s, t):

        if len(s) == 0:
            return True

        l = 0
        r = 0
        ans = ""

        while l < len(s) and r < len(t):

            if s[l] == t[r]:
                ans += s[l]
                l += 1

            r += 1

            if len(ans) == len(s):
                return True

        return False