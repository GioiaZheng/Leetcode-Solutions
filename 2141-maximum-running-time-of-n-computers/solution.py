class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """
        We want to run n computers for the same number of minutes.
        Since batteries can be swapped freely, each battery can contribute
        at most 't' minutes to the total pool.

        Core idea:
        - Binary search on possible running time t.
        - For a given t, compute total usable minutes:
              sum(min(b, t) for b in batteries)
        - If total >= n * t, then t is feasible.
        """

        def can_run(t):
            """
            Check if we can run n computers for t minutes.
            Each battery contributes min(battery, t).
            We need total contribution >= n * t.
            """
            total = 0
            for b in batteries:
                total += min(b, t)
                # Early stop if enough
                if total >= t * n:
                    return True
            return total >= t * n

        # Binary search
        left, right = 0, sum(batteries) // n

        while left < right:
            # upper mid to avoid infinite loop
            mid = (left + right + 1) // 2

            if can_run(mid):
                left = mid
            else:
                right = mid - 1

        return left
