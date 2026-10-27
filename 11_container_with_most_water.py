class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        V_max = 0
        while left < right:
            V = min(height[left], height[right]) * (right - left)
            # print(V)
            if V > V_max:
                V_max = V
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return V_max

height = [1,8,6,2,5,4,8,3,7]
sol = Solution()
ans = sol.maxArea(height)
print(ans)