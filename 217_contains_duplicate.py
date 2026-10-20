class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False

sol = Solution()
nums = [1, 2, 3, 4]
ans = sol.containsDuplicate(nums)
print(ans)