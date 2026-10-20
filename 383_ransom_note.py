class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        records = {}
        for c in magazine:
            if c not in records:
                records[c] = 1
            else:
                records[c] += 1

        for c in ransomNote:
            if c not in records:
                return False
            else:
                records[c] -= 1
                if records[c] < 0:
                    return False
        return True

ransomNote = "aaasdad"
magazine = "aabadsas"

sol = Solution()
result = sol.canConstruct(ransomNote, magazine)
print(result)