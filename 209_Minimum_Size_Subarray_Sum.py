class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        current_sub_len = len(nums)
        min_len = 0
        while current_sub_len > 0:
            for iter_len in range(len(nums)-current_sub_len+1):
                sub_sum = sum(nums[0+iter_len:current_sub_len+iter_len])
                print(nums[0+iter_len:current_sub_len+iter_len], sub_sum)
                if sub_sum >= target:
                    min_len = current_sub_len
                    break
            current_sub_len -= 1
        return min_len
    def minSubArrayLen2(self, target: int, nums: list[int]) -> int:

        left = 0
        right = 1
        min_len = len(nums) + 1
        sub_sum = sum(nums[left:right])
        while right <= len(nums):
            print(nums[left:right], sub_sum)
            if sub_sum < target:
                if right == len(nums):
                    break
                sub_sum += nums[right]
                right += 1
            elif sub_sum >= target:
                if right - left < min_len:
                    min_len = right - left
                sub_sum -= nums[left]
                left += 1
            print(nums[left:right], sub_sum)

        return min_len if min_len < len(nums) + 1 else 0

target = 7
nums = [2,3,2,1,4,3]
# target = 4
# nums = [1,4,4]
target = 11
nums = [1,1,1,1,1,1,1,1]
sol = Solution()
ans = sol.minSubArrayLen2(target, nums)
print(ans)