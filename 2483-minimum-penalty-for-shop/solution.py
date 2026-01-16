class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Initial penalty: close at hour 0
        # All 'Y' after closing cause penalty
        penalty = customers.count('Y')
        min_penalty = penalty
        best_hour = 0

        # Scan hour by hour
        for i, c in enumerate(customers):
            if c == 'Y':
                # We stay open this hour instead of closed -> one less penalty
                penalty -= 1
            else:
                # We stay open but no customers -> one more penalty
                penalty += 1

            # Closing at hour i+1
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = i + 1

        return best_hour
