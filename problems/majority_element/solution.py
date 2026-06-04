class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        for i in range(0,len(nums)):
            if count==0:
                majorityelem=nums[i]
                count=1
            else:
                if nums[i]==majorityelem:
                    count+=1
                else:
                    count-=1
        return majorityelem