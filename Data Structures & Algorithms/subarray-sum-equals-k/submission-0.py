class Solution:
    def subarraySum(self, nums, k):

        n = len(nums)

        count = 0

        prefixSum = [0] * n

        # Build Prefix Sum Array
        prefixSum[0] = nums[0]

        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]

        freq = {}

        for j in range(n):

            if prefixSum[j] == k:
                count += 1

            val = prefixSum[j] - k

            if val in freq:
                count += freq[val]

            if prefixSum[j] in freq:
                freq[prefixSum[j]] += 1
            else:
                freq[prefixSum[j]] = 1

        return count