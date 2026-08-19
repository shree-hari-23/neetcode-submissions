class Solution:
    def check(self, arr):
       N=len(arr)
       count=0
       for i in range(N):
           if arr[i]>arr[(i+1)%N]:
              count+=1
       if count<=1:
            return True
       return False
            

   