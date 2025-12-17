class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow
            if rev > INT_MAX // 10 or \
               (rev == INT_MAX // 10 and digit > 7):
                return 0

            rev = rev * 10 + digit

        return sign * rev
