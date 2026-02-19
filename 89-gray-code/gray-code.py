class Solution:
    def grayCode(self, n: int) -> List[int]:
        res=[]
        for i in range(2**n):
            k=i^(i>>1)
            res.append(k)
        return res
