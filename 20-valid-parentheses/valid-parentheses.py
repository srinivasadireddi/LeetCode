class Solution:
    def isValid(self, s: str) -> bool:
        hashMap={ ')':'(', ']':'[','}':'{' }
        stack=[]
        for c in s:
            if c not in hashMap:
                #has to be an open bracket
                stack.append(c)
            else:
                if not stack:
                    return False
                popped= stack.pop()
                if popped != hashMap[c]:
                    return False
        return not stack

        