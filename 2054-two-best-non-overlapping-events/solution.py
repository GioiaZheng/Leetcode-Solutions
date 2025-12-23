from typing import List
import bisect

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by start time
        events.sort(key=lambda x: x[0])

        n = len(events)

        # starts[i] = events[i][0]
        starts = [e[0] for e in events]

        # suffix_max[i] = max value among events[i:]
        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], events[i][2])

        ans = 0

        for i in range(n):
            start, end, value = events[i]

            # Take only this event
            ans = max(ans, value)

            # Find the first event that starts at or after end + 1
            j = bisect.bisect_left(starts, end + 1)

            # Combine with the best possible second event
            if j < n:
                ans = max(ans, value + suffix_max[j])

        return ans
