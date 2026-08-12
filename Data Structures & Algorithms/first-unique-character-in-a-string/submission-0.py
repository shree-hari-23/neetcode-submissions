class Solution:

    def firstUniqChar(self, s):

        freq = {}

        # Count frequency
        for ch in s:

            if ch in freq:
                freq[ch] += 1

            else:
                freq[ch] = 1

        # Find first unique character
        for i in range(len(s)):

            if freq[s[i]] == 1:
                return i

        return -1