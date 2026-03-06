class Solution:
    def separateSquares(self, squares):
        # Total area
        total_area = 0
        min_y = float('inf')
        max_y = 0
        
        for _, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)
        
        target = total_area / 2
        
        def area_below(h):
            area = 0.0
            for _, y, l in squares:
                if h <= y:
                    continue
                elif h >= y + l:
                    area += l * l
                else:
                    area += l * (h - y)
            return area
        
        low, high = min_y, max_y
        
        for _ in range(60):  # sufficient for 1e-5 precision
            mid = (low + high) / 2
            if area_below(mid) < target:
                low = mid
            else:
                high = mid
        
        return low
