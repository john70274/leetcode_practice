class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = {}
        zero_seen = []
        for num in nums1:
            seen[num] = 0
        for num in nums2:
            if num in seen:
                seen[num] += 1
        for key in seen.keys():
            if seen[key] == 0:
                zero_seen.append(key)
        seen_list = list(seen.keys())
        for num in zero_seen:
            seen_list.remove(num)
        return seen_list

    def intersection2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = {}
        result = []
        for num in nums1:
            seen[num] = 0
        for num in nums2:
            if num in seen:
                seen[num] += 1
        for key in seen.keys():
            if seen[key] > 0:
                result.append(key)
        return result

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

sol = Solution()

print(sol.intersection2(nums1, nums2))
