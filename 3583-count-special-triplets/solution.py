from collections import Counter

MOD = 10**9 + 7

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        rightCount = Counter(nums)   # all elements start on the right side
        leftCount = Counter()        # left side is initially empty
        
        ans = 0
        
        for j in range(len(nums)):
            val_j = nums[j]
            rightCount[val_j] -= 1   # nums[j] is no longer on the right
            
            need = val_j * 2
            
            # Count valid i and k
            count_left = leftCount[need]
            count_right = rightCount[need]
            
            ans = (ans + count_left * count_right) % MOD
            
            leftCount[val_j] += 1    # move nums[j] to the left
        
        return ans
