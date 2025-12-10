MOD = 10**9 + 7

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)

        # Step 1: group by complexity value
        from collections import defaultdict
        groups = defaultdict(list)
        for i, c in enumerate(complexity):
            groups[c].append(i)

        # Step 2: sort by complexity
        layers = []
        for c in sorted(groups.keys()):
            layers.append(groups[c])

        # Step 3: check feasibility
        min_index = float('inf')
        for layer in layers:
            for idx in layer:
                if idx != 0 and all(complexity[j] >= complexity[idx] for j in range(idx)):
                    return 0

        # Step 4: combinatorics
        # Precompute factorials
        fact = [1] * (n + 1)
        inv = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i-1] * i % MOD

        inv[n] = pow(fact[n], MOD-2, MOD)
        for i in reversed(range(n)):
            inv[i] = inv[i+1] * (i+1) % MOD

        def C(a, b):
            if a < b: return 0
            return fact[a] * inv[b] % MOD * inv[a-b] % MOD

        total = 0
        ans = 1
        for layer in layers:
            k = len(layer)
            if total == 0:
                if layer[0] != 0:
                    return 0
            else:
                ans = ans * C(total + k - 1, k) % MOD
            total += k

        return ans
