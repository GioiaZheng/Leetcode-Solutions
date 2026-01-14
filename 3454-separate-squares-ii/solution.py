from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # --- Step 1: Build events and collect x-coordinates ---
        events = []  # (y, type, x1, x2), type: +1 add, -1 remove
        xs = set()

        for x, y, l in squares:
            x1, x2 = x, x + l
            y1, y2 = y, y + l
            events.append((y1, 1, x1, x2))
            events.append((y2, -1, x1, x2))
            xs.add(x1)
            xs.add(x2)

        # Coordinate compression on x
        xs = sorted(xs)
        x_index = {x: i for i, x in enumerate(xs)}

        # --- Step 2: Segment Tree for union length ---
        n = len(xs) - 1  # intervals between xs[i] and xs[i+1]

        count = [0] * (4 * n)
        length = [0] * (4 * n)

        def push_up(node, l, r):
            if count[node] > 0:
                length[node] = xs[r + 1] - xs[l]
            elif l == r:
                length[node] = 0
            else:
                length[node] = length[node * 2] + length[node * 2 + 1]

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                count[node] += val
                push_up(node, l, r)
                return
            mid = (l + r) // 2
            if ql <= mid:
                update(node * 2, l, mid, ql, qr, val)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, val)
            push_up(node, l, r)

        # --- Step 3: Sweep line to compute total union area ---
        events.sort()
        total_area = 0.0
        prev_y = events[0][0]
        cur_x_len = 0.0

        for y, typ, x1, x2 in events:
            dy = y - prev_y
            if dy > 0:
                total_area += cur_x_len * dy

            l = x_index[x1]
            r = x_index[x2] - 1
            if l <= r:
                update(1, 0, n - 1, l, r, typ)

            cur_x_len = length[1]
            prev_y = y

        target = total_area / 2

        # --- Step 4: Sweep again to find minimal y reaching half area ---
        count = [0] * (4 * n)
        length = [0] * (4 * n)

        prev_y = events[0][0]
        cur_x_len = 0.0
        area_below = 0.0

        for y, typ, x1, x2 in events:
            dy = y - prev_y
            if dy > 0:
                slice_area = cur_x_len * dy
                if area_below + slice_area >= target:
                    # interpolate inside this slice
                    need = target - area_below
                    return prev_y + need / cur_x_len
                area_below += slice_area

            l = x_index[x1]
            r = x_index[x2] - 1
            if l <= r:
                update(1, 0, n - 1, l, r, typ)

            cur_x_len = length[1]
            prev_y = y

        return prev_y
