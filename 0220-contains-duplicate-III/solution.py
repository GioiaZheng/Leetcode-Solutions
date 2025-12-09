class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        
        bucket = {}
        size = valueDiff + 1  # bucket size
        
        for i, num in enumerate(nums):
            bucket_id = num // size
            
            # 1. same bucket
            if bucket_id in bucket:
                return True
            
            # 2. neighbor buckets
            if bucket_id - 1 in bucket and abs(num - bucket[bucket_id - 1]) <= valueDiff:
                return True
            if bucket_id + 1 in bucket and abs(num - bucket[bucket_id + 1]) <= valueDiff:
                return True
            
            # place current number
            bucket[bucket_id] = num
            
            # 3. maintain window size (remove old element)
            if i >= indexDiff:
                old_bucket = nums[i - indexDiff] // size
                del bucket[old_bucket]
        
        return False
