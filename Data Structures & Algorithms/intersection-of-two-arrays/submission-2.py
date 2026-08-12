class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #set1=set(nums1)
        #set2=set(nums2)
        #return list(set1.intersection(set2))
        nums1.sort()
        nums2.sort()
        ans=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j] :
                    if len(ans) == 0 or ans[-1] != nums1[i]:
                      ans.append(nums1[i])
                      break
        return ans