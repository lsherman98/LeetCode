class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        mid_idx = len(nums) // 2
        if nums[mid_idx] == target:
            return mid_idx
        
        if nums[mid_idx] < target:
            res = self.search(nums[mid_idx+1:], target)
            if res < 0:
                return res
            return res + 1 + mid_idx
        else:
            return self.search(nums[0:mid_idx], target)