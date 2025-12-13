from typing import List

class Solution:
    def validateCoupons(
        self,
        code: List[str],
        businessLine: List[str],
        isActive: List[bool]
    ) -> List[str]:

        valid_lines = {"electronics", "grocery", "pharmacy", "restaurant"}
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        valid = []

        for c, b, active in zip(code, businessLine, isActive):
            if not active:
                continue
            if not c:
                continue
            if not all(ch.isalnum() or ch == "_" for ch in c):
                continue
            if b not in valid_lines:
                continue

            valid.append((order[b], c))

        valid.sort()
        return [c for _, c in valid]
