class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ls = []
        for i in words:
            words_check = [j for j in words if j!=i]
            for k in words_check:
                if i in k:
                    ls.append(i)
        return list(set(ls))


        