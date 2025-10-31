class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        numcounts={}
        sneakynums=[]
        for i in range(0,len(nums)):
            if nums[i] in numcounts:
                numcounts[nums[i]]+=1
            else:
                numcounts[nums[i]]=1
        for key,value in numcounts.items():
            if value==2:
                sneakynums.append(key)
        return sneakynums