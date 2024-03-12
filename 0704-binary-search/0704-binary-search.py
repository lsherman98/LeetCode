class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        mid_idx = len(nums) // 2 
        if nums[mid_idx] == target:
            return mid_idx
        
        if target > nums[mid_idx]:
            res = self.search(nums[mid_idx + 1:], target) 
            if res < 0:
                return res
            else:
                return res + mid_idx + 1
        else:
            return self.search(nums[0:mid_idx], target)
        
        
    
    