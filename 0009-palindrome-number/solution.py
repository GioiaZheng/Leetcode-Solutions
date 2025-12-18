class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Numbers ending with 0 (except 0 itself) are not palindromes
        if x != 0 and x % 10 == 0:
            return False

        reversed_half = 0

        # Reverse only half of the number
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even length: x == reversed_half
        # For odd length:  x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
