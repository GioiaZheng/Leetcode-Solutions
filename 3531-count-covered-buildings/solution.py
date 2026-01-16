class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        from collections import defaultdict
        
        # For each row and column, store min and max
        row_min = defaultdict(lambda: float('inf'))
        row_max = defaultdict(lambda: -float('inf'))
        col_min = defaultdict(lambda: float('inf'))
        col_max = defaultdict(lambda: -float('inf'))

        # First pass: compute min/max for each row and column
        for x, y in buildings:
            row_min[x] = min(row_min[x], y)
            row_max[x] = max(row_max[x], y)
            col_min[y] = min(col_min[y], x)
            col_max[y] = max(col_max[y], x)

        # Second pass: count covered buildings
        covered = 0
        for x, y in buildings:
            has_left = row_min[x] < y
            has_right = row_max[x] > y
            has_above = col_min[y] < x
            has_below = col_max[y] > x

            # Covered means at least one building in all four directions.
            if has_left and has_right and has_above and has_below:
                covered += 1

        return covered
