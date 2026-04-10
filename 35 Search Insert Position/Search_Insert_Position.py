class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search approach
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left+right) // 2
            
            if target == nums[mid]:
                return mid # element found in array
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return left # element doesn't exist, so returing her idx number
