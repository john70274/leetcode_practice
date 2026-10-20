class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        h = 0
        t = len(s) - 1
        while h < t:
            s[h], s[t] = s[t], s[h]
            # print(s)
            h += 1
            t -= 1
        return

s = ["h","e","l","l","o"]
sol = Solution()
ans = sol.reverseString(s)
print(s)