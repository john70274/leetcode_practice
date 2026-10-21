class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 1
        fast = 1
        variety = 1
        last_num = nums[0]
        while slow < len(nums) and fast < len(nums):
            # print(slow, nums[slow], fast, nums[fast], last_num)
            # print(variety)
            # print(nums)
            if last_num != nums[fast]:
                variety += 1
                last_num = nums[fast]
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                # print(nums)
            fast += 1
        return variety


nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2]
nums = [1,1,1,1,1,1,2,2,3,3,4,4,5,6,6,7,7,7,7]
sol = Solution()
ans = sol.removeDuplicates(nums)
print(ans, nums)