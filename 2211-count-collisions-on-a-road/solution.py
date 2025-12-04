class Solution:
    def countCollisions(self, directions: str) -> int:
        # 1. Remove leading 'L' cars (they move left forever and never collide)
        directions = directions.lstrip('L')

        # 2. Remove trailing 'R' cars (they move right forever and never collide)
        directions = directions.rstrip('R')

        # 3. In the remaining middle segment:
        #    Every 'L' or 'R' must eventually collide and become stationary.
        #    Only 'S' causes no collision.
        #    Therefore, the number of collisions equals the count of non-'S'.
        return sum(c != 'S' for c in directions)
