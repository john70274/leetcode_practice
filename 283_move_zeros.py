class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0
        while fast < len(nums):
            # print(slow, fast, nums)
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0:
                slow += 1
            fast += 1
            # print(slow, fast, nums)



nums = [2, 1]
# nums = [2,1,0,3,12]
nums = [1,0,3]
sol = Solution()
sol.moveZeroes(nums)
print(nums)