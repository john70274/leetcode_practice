class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bra_mapping = {'(', '[', '{'}
        ket_mapping = {')': '(', ']': '[', '}': '{'}
        for c in s:
            # print(c)
            # print(stack)
            if c in bra_mapping:
                stack.append(c)
            elif c in ket_mapping:
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] == ket_mapping[c]:
                        stack.pop()
                    else:
                        return False
            # print(stack)

        if stack == []:
            return True
        else:
            return False
