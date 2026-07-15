class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        if m==0:
            return False
        l=0
        r=m*n-1
        while l<=r:
            mid=(l+r)//2
            e=matrix[mid//n][mid%n]
            if target==e:
                return True
            elif target<e:
                r=mid-1
            else:
                l=mid+1
        return False

             

        