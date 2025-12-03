from collections import defaultdict
from math import gcd
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        """
        Count trapezoids:
        
        Trapezoids = (quadrilaterals with ≥1 parallel side) − (parallelograms)

        where:
        - parallel lines are detected by slope + intercept grouping
        - parallelograms are detected by midpoint counting (via vector direction)
        """
        n = len(points)

        # Groups to detect parallel lines
        t = defaultdict(lambda: defaultdict(int))

        # Groups to detect parallelograms
        v = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                # Normalize direction (dx > 0) or (dx == 0 and dy > 0)
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy

                # Reduce slope
                g = gcd(dx, abs(dy))
                sx = dx // g
                sy = dy // g

                # Line constant: sx*y - sy*x
                const = sx * y1 - sy * x1

                # Encode slope and direction
                slope_key = (sx << 16) | (sy + 10000)
                dir_key   = (dx << 16) | (dy + 10000)

                # Update maps
                t[slope_key][const] += 1
                v[dir_key][const] += 1

        def count_pairs(mp: dict) -> int:
            """
            Count Σ ci * cj for i < j using prefix subtraction.
            """
            ans = 0
            for inner in mp.values():
                counts = list(inner.values())
                total = sum(counts)
                rem = total
                for c in counts:
                    rem -= c
                    ans += c * rem
            return ans

        parallel_pairs = count_pairs(t)
        parallelogram_pairs = count_pairs(v) // 2  # counted twice

        return parallel_pairs - parallelogram_pairs
