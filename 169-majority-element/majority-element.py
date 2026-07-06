class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        ma=nums[0]

        for nums in nums:
            if nums==ma:
                count+=1
            else:
                count-=1
                if count==0:
                    ma=nums
                    count=1


        return ma
     
           

        