class Solution:
    def removeDuplicates_On2(self, s: str) -> str:
        s_list = []
        for c in s:
            s_list.append(c)

        p = 1
        seen = s_list[0]
        while p < len(s_list):
            print(p, seen, s_list[p])
            print('b', s_list)
            if s_list[p] == seen:
                s_list.pop(p)
                s_list.pop(p-1)
                p -= 1
                if p - 1 >= 0:
                    p -= 1
                if s_list == []:
                    return ''
                print('a', s_list)
            seen = s_list[p]
            p += 1

        return ''.join(s_list)

    def removeDuplicates(self, s: str) -> str:
        processed = []
        for c in s:
            if len(processed) == 0:
                processed.append(c)
            else:
                if processed[-1] == c:
                    processed.pop(-1)
                else:
                    processed.append(c)
        return ''.join(processed)

s = "abbaca"
# s = "azxxzy"
s = "azxxzyccd"
sol = Solution()
ans = sol.removeDuplicates(s)
print(ans)