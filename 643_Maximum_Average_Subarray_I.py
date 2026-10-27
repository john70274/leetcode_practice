class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = sum(nums[0:k])
        current_sum = sum(nums[0:k])
        # print(max_sum)
        slow = 0
        fast = k
        while fast < len(nums):
            # print(slow, fast, nums[slow], nums[fast])
            current_sum = current_sum  - nums[slow] + nums[fast]
            # print(current_sum)
            if max_sum < current_sum:
                max_sum = current_sum
            slow += 1
            fast += 1
        return max_sum/k