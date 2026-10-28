class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_product = 1
        left_product_list = []
        for i, num in enumerate(nums):
            if i == 0:
                left_product_list.append(1)
            else:
                left_product = left_product * nums[i-1]
                left_product_list.append(left_product)

        right_product = 1
        right_product_list = []
        nums = nums[::-1]
        for i, num in enumerate(nums):
            if i == 0:
                right_product_list.append(1)
            else:
                right_product = right_product * nums[i-1]
                right_product_list.append(right_product)

        print(left_product_list)
        print(right_product_list)
        product_list = []
        right_product_list = right_product_list[::-1]
        for i in range(len(left_product_list)):
            product = left_product_list[i] * right_product_list[i]
            product_list.append(product)
        print(product_list)
        return product_list
nums = [-1,1,0,-3,3]
nums = [1,2,3,4]
sol = Solution()
ans = sol.productExceptSelf(nums)
print(ans)