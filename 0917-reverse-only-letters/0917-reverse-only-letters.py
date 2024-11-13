class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = list(s)
        s = 0
        e = len(l) - 1

        while s < e:
            while s < e and not l[e].isalpha():
                e -= 1
            while s < e and not l[s].isalpha():
                s += 1
            l[s], l[e] = l[e], l[s]
            s += 1
            e -= 1
        
        return ''.join(l)