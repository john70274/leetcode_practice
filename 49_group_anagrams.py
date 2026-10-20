class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = {}
        for s in strs:
            elements = [0] * 26
            for c in s:
                elements[ord(c)-97] += 1
            elements = tuple(elements)
            if elements not in result:
                result[elements] = [s]
            else:
                result[elements].append(s)

        return list(result.values())

strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
print(sol.groupAnagrams(strs))