class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        for c in s:
            if c not in char_count:
                char_count[c] = 0
            char_count[c] += 1

        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i

        return -1