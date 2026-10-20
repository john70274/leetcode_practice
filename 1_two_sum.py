class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                return [seen[nums[i]], i]
            else:
                seen[target-nums[i]] = i
        return None

nums = [3,3]
target = 6
sol = Solution()
print(sol.twoSum(nums, target))