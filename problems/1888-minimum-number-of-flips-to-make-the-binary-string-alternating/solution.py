class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        # For even length, rotation does not change which alternating pattern
        # each index should match, so we can compare directly.
        if n % 2 == 0:
            diff1 = 0  # mismatches against pattern "0101..."
            diff2 = 0  # mismatches against pattern "1010..."
            for i, ch in enumerate(s):
                expected1 = '0' if i % 2 == 0 else '1'
                expected2 = '1' if i % 2 == 0 else '0'
                if ch != expected1:
                    diff1 += 1
                if ch != expected2:
                    diff2 += 1
            return min(diff1, diff2)

        # For odd length, rotations matter.
        # Double the string and use a sliding window of size n.
        ss = s + s
        diff1 = 0  # mismatches against "0101..."
        diff2 = 0  # mismatches against "1010..."
        ans = n

        left = 0
        for right in range(2 * n):
            expected1 = '0' if right % 2 == 0 else '1'
            expected2 = '1' if right % 2 == 0 else '0'

            if ss[right] != expected1:
                diff1 += 1
            if ss[right] != expected2:
                diff2 += 1

            # Keep window size at most n
            if right - left + 1 > n:
                left_expected1 = '0' if left % 2 == 0 else '1'
                left_expected2 = '1' if left % 2 == 0 else '0'

                if ss[left] != left_expected1:
                    diff1 -= 1
                if ss[left] != left_expected2:
                    diff2 -= 1
                left += 1

            # Evaluate each rotation window
            if right - left + 1 == n:
                ans = min(ans, diff1, diff2)

        return ans
