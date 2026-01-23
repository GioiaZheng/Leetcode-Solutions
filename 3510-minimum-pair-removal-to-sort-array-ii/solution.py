from typing import List
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # ---------- Step 1: 初始化双向链表 ----------
        prev = [i - 1 for i in range(n)]
        nxt = [i + 1 if i + 1 < n else -1 for i in range(n)]
        removed = [False] * n

        # ---------- Step 2: 统计当前逆序对数量 ----------
        bad = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                bad += 1

        if bad == 0:
            return 0

        # ---------- Step 3: 建立最小堆（相邻 pair） ----------
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        ops = 0

        # ---------- Step 4: 强制合并过程 ----------
        while bad > 0:
            # 找到当前仍然有效、且 sum 匹配的 pair
            while True:
                pair_sum, i = heapq.heappop(heap)
                if removed[i] or nxt[i] == -1:
                    continue
                j = nxt[i]
                if removed[j]:
                    continue
                if nums[i] + nums[j] != pair_sum:
                    continue
                break

            j = nxt[i]
            pi = prev[i]
            nj = nxt[j]

            # ---------- Step 4.1: 移除旧的逆序贡献 ----------
            if pi != -1 and nums[pi] > nums[i]:
                bad -= 1
            if nums[i] > nums[j]:
                bad -= 1
            if nj != -1 and nums[j] > nums[nj]:
                bad -= 1

            # ---------- Step 4.2: 合并 i 和 j ----------
            nums[i] += nums[j]
            removed[j] = True

            nxt[i] = nj
            if nj != -1:
                prev[nj] = i

            # ---------- Step 4.3: 添加新的逆序贡献 ----------
            if pi != -1 and nums[pi] > nums[i]:
                bad += 1
            if nj != -1 and nums[i] > nums[nj]:
                bad += 1

            # ---------- Step 4.4: 更新堆 ----------
            if pi != -1:
                heapq.heappush(heap, (nums[pi] + nums[i], pi))
            if nj != -1:
                heapq.heappush(heap, (nums[i] + nums[nj], i))

            ops += 1

        return ops
