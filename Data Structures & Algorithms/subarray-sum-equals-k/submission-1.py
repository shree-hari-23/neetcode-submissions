class Solution:
    def subarraySum(self, nums, k):

        n = len(nums)
        count = 0
        prefixsum=[]
        prefixsum.append(nums[0])
        for i in range(1,n):
            prefixsum.append(prefixsum[i-1]+nums[i])
        freq={}
        for j in range(n):
            if prefixsum[j]==k:
                count+=1
            val=prefixsum[j]-k
            if val in freq:
                count+=freq[val]
            if prefixsum[j] in freq:
                freq[prefixsum[j]]+=1
            else:
                freq[prefixsum[j]]=1
        return count


