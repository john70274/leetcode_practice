from re import search


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            sq_mid = mid * mid
            if sq_mid < x:
                left = mid + 1
            elif sq_mid > x:
                right = mid - 1
            elif sq_mid == x:
                return mid

        return right


x = 4
sol = Solution()
ans = sol.mySqrt(x)
print(ans)