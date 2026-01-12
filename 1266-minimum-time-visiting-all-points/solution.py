class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        
        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]
            
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            
            total_time += max(dx, dy)
        
        return total_time
