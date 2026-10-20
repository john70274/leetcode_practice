class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        while left < right:
            while not s[left].isalnum():
                left += 1
            while not s[right].isalnum():
                right -= 1
            # print(s[left].lower(), s[right].lower(), s[left].lower() == s[right].lower())
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True

s = "A man, a plan, a canal: Panama"
# s = "race a car"
s = " "
sol = Solution()
print(sol.isPalindrome(s))