class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            print('left: ', left, 'mid: ', mid, 'right: ', right)
            print(nums[left] , nums[mid], nums[right])
            if nums[left] > nums[mid]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return nums[left]
        return nums[left]

nums = [3,4,5,1,2]
sol = Solution()
ans = sol.findMin(nums)
print(ans)