class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
        
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        bucket_min = [float('inf')] * bucket_count
        bucket_max = [-float('inf')] * bucket_count
        
        for num in nums:
            idx = (num - min_val) // bucket_size
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)
        
        max_gap = 0
        prev = min_val
        
        for i in range(bucket_count):
            if bucket_min[i] == float('inf'):
                continue
            
            max_gap = max(max_gap, bucket_min[i] - prev)
            prev = bucket_max[i]
        
        return max_gap
