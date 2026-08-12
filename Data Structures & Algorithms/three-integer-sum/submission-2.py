class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    triplet = [nums[i], nums[left], nums[right]]

                    if triplet not in ans:
                        ans.append(triplet)

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return ans