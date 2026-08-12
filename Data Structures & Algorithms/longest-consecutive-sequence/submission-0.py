class Solution:
    def longestConsecutive(self, nums):

        if len(nums) == 0:
            return 0

        nums.sort()

        l = 0
        count = 1
        ans = 1

        for r in range(1, len(nums)):

            # Duplicate number, ignore it
            if nums[r] == nums[r - 1]:
                continue

            # Consecutive number
            if nums[r] == nums[r - 1] + 1:
                count += 1

            # Sequence breaks
            else:
                count = 1

            ans = max(ans, count)

        return ans