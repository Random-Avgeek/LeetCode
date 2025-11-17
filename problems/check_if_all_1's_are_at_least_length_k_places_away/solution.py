class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count=0
        onespotted=False
        for i in range(0,len(nums)):
            if nums[i]==1 and onespotted==False:
                onespotted=True
                count=0
            elif nums[i]==0 and onespotted==True:
                count+=1
            elif nums[i]==1 and onespotted==True:
                if count<k:
                    return False
                else:
                    count=0
        return True