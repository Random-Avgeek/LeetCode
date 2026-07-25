class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        if len(points)<=2:
            return len(points)
        def slope(p1,p2):
            dx=p1[0]-p2[0]
            dy=p1[1]-p2[1]
            if dx==0:
                return (1,0)
            elif dy==0:
                return(0,1)
            g=gcd(abs(dx),abs(dy))
            dx//=g
            dy//=g
            if dx<0:
                dx,dy=-dx,-dy
            return (dy,dx)
        all_max=1
        for i in range(len(points)):
            if len(points)-i < all_max: break
            slope_map={}
            anchor=points[i]
            for j in range(i+1,len(points)):
                slope_key=slope(anchor,points[j])
                slope_map[slope_key]=slope_map.get(slope_key,0)+1
                all_max=max(slope_map[slope_key]+1,all_max)
        return all_max
