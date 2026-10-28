class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        right_sum = sum(nums[1:])
        print("left_sum: ", left_sum, "right_sum: ", right_sum)
        if left_sum == right_sum:
            return 0
        for pointer in range(1, len(nums)):
            left_sum += nums[pointer-1]
            right_sum -= nums[pointer]
            print("left_sum: ",left_sum, "right_sum: ",right_sum)
            if left_sum == right_sum:
                return pointer

        return -1

nums = [1, 7, 3, 6, 5, 6, 1, 1, 4, 1, 3, 5, 1, 1]
nums = [1]
# nums = [1,2,3]
# nums = [2,1,-1]
# nums = [10, 2, 1, -1, 5, 3, 7, 8, 11, 9, 2, -10]
sol = Solution()
ans = sol.pivotIndex(nums)
print(ans)