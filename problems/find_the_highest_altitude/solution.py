class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height=0
        maxheight=0
        for jump in gain:
            if jump<0:
                height+=jump
                continue
            else:
                height+=jump
                maxheight=max(height,maxheight)
        return maxheight
