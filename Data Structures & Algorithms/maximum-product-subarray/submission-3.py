class Solution:
    def maxProduct(self, nums):

        n = len(nums)

        leftProd = 1
        rightProd = 1

        ans = nums[0]

        for i in range(n):

            if leftProd == 0:
                leftProd = 1

            if rightProd == 0:
                rightProd = 1

            leftProd *= nums[i]
            rightProd *= nums[n - 1 - i]

            ans = max(ans, leftProd, rightProd)

        return ans