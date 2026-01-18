class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        self.count = 0

        def dfs(node, parent):
            total = values[node]
            for nei in graph[node]:
                if nei == parent:
                    continue
                total += dfs(nei, node)

            if total % k == 0:
                self.count += 1
                return 0
            return total

        dfs(0, -1)
        return self.count
