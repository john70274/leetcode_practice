class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for c in s:
            if c in seen:
                seen[c] += 1
            else:
                seen[c] = 1
        for c in t:
            if c in seen:
                seen[c] -= 1
                if seen[c] < 0:
                    return False
            else:
                return False
        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        seen = [0] * 26
        if len(s) != len(t):
            return False
        else:
            for c in s:
                seen[ord(c)-97] += 1
            for c in t:
                seen[ord(c)-97] -= 1
            return seen == [0] * 26

s = "rat"
t = "car"
sol = Solution()
ans = sol.isAnagram2(s, t)
print(ans)