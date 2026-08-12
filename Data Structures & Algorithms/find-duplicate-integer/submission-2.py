class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
            if freq[nums[i]]!=1:
                return nums[i]
        
            