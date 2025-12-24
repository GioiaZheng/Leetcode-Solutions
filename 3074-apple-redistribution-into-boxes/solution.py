from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # Total number of apples
        total_apples = sum(apple)

        # Sort box capacities in descending order
        capacity.sort(reverse=True)

        used = 0
        current_capacity = 0

        # Greedily take the largest boxes first
        for cap in capacity:
            current_capacity += cap
            used += 1
            if current_capacity >= total_apples:
                return used

        return used
