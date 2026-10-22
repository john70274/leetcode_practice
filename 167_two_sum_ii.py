class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            pair_sum = numbers[left] + numbers[right]
            if pair_sum == target:
                return [left + 1, right + 1]
            elif pair_sum > target:
                right -= 1
            elif pair_sum < target:
                left += 1
        return

numbers = [2, 3, 4, 5, 6, 7, 11, 15]
target = 9

# numbers = [1, 2, 3, 4, 5, 7, 8, 10, 16]
# target = 6

# numbers = [-1,0]
# target = -1
sol = Solution()
ans = sol.twoSum(numbers, target)
print(ans)