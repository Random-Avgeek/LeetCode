import random
class Solution:

    def __init__(self, nums: List[int]):
        self.ognums=list(nums)
        self.curr=nums

    def reset(self) -> List[int]:
        self.curr=list(self.ognums)
        return self.curr

    def shuffle(self) -> List[int]:
        for i in range(len(self.curr)):
            swapid=random.randrange(i,len(self.curr))
            self.curr[i],self.curr[swapid]=self.curr[swapid],self.curr[i]
        return self.curr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()