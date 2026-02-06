class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        le=0
        rh=len(nums)-1
        while le<=rh:
            mid=(le+rh)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                rh=mid-1
            else:
                le=mid+1
        return le


        