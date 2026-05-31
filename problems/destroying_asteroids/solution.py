class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids=sorted(asteroids)
        newmass=mass
        for i in range(len(asteroids)):
            if asteroids[i]<=newmass:
                newmass+=asteroids[i]
            elif asteroids[i]>newmass:
                return False
        return True