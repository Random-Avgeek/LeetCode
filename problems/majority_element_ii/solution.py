class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        results=[]
        if len(nums)==1:
            return [nums[0]]
        candidate1=None
        candidate2=None
        count1=0
        count2=0
        for i in range(len(nums)):
            if nums[i]==candidate1:
                count1+=1
            elif nums[i]==candidate2:
                count2+=1
            elif count1==0:
                candidate1=nums[i]
                count1=1
            elif count2==0:
                candidate2=nums[i]
                count2=1
            else:
                count1-=1
                count2-=1
        freq1=0
        freq2=0
        for num in nums:
            if num==candidate1:
                freq1+=1
            elif num==candidate2:
                freq2+=1
        if freq1>len(nums)//3:
            results.append(candidate1)
        if freq2>len(nums)//3:
            results.append(candidate2)
        return results