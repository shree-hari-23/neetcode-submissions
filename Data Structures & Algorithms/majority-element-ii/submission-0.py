class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        freq={}
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
            ans=[]
        for key in freq:
            if freq[key]>n//3:
                ans.append(key)
        return ans
            
           
        