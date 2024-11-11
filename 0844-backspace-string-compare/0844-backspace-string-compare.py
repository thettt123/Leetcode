class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = ''
        b = ''
        for i in s:
            if i != '#':
                a += i
            else:
                a = a[:-1:]
        for j in t:
            if j != '#':
                b += j
            else:
                b = b[:-1:]
        return a == b