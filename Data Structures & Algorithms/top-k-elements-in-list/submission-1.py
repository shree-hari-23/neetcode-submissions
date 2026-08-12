class Solution:
    def topKFrequent(self, nums, k):

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        ans = []

        while k > 0:

            maxNum = 0
            maxCount = 0

            for num, count in freq.items():

                if count > maxCount:
                    maxCount = count
                    maxNum = num

            ans.append(maxNum)

            del freq[maxNum]

            k -= 1

        return ans