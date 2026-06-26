class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis=[]
        for point in points:
            x,y = point[0],point[1]
            distance = x*x+y*y
            heapq.heappush(dis,(-distance,[x,y]))
            if len(dis) > k:
                heapq.heappop(dis)
        heapq.heapify(dis)
        while len(dis) > k:
            heapq.heappop(dis)
        ans = []
        while len(dis) != 0:
            distance,point = heapq.heappop(dis)
            ans.append(point)
        return ans
        
        
