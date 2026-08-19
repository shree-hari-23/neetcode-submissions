class Solution:
    def check(self, arr):
        N=len(arr)
        count=1
        for i in range(1,2*N):
            if arr[(i-1)%N]<=arr[(i)%N]:
                count+=1
            else:
                count=1
            if count==N:
                return True
        return False