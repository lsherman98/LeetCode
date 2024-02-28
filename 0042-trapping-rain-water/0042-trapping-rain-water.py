class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        l, r = 0, len(height) - 1
        l_bound, r_bound = 0, 0 
        
        while l < r:
            if height[l] <= height[r]:
                l_bound = max(l_bound, height[l])
                total_water += l_bound - height[l]
                l += 1
            else:
                r_bound = max(r_bound, height[r])
                total_water += r_bound - height[r]
                r -= 1
                
        return total_water