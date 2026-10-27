class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        # right = 1
        longestLen = 0
        seen = {}
        for right, c in enumerate(s):
            print('l, r: ', left, right)
            print(s[left:right+1], c)
            currentLen = right - left + 1
            if c not in seen:
                seen[c] = right
                print(seen)
                if currentLen > longestLen:
                    longestLen = currentLen
            else:
                temp_pointer = seen[c] + 1
                print(seen)
                while left < temp_pointer:
                    print(left, c, temp_pointer)
                    print('delete: ', s[left])
                    seen.pop(s[left])
                    print(seen)
                    left += 1
                seen[c] = right
                print(c)


        return longestLen

s= "pwwkew"
s = "bbbbb"
s = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))