class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: no zigzag possible
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curr_row = 0
        direction = -1  # will flip at top/bottom

        for ch in s:
            rows[curr_row] += ch

            # change direction at first or last row
            if curr_row == 0 or curr_row == numRows - 1:
                direction *= -1

            curr_row += direction

        return "".join(rows)
