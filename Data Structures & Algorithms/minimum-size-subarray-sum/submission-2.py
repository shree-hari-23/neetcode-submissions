class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        l=0
        mini=float('inf')
        total=0
        for r in range(n):
            total+=nums[r]
            while total>=target:
                mini=min(mini,r-l+1)
                total-=nums[l]
                l+=1
                
        if mini==float('inf'):
           return 0
        return mini
       