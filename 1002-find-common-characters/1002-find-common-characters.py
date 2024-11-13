class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s = Counter(words[0])
        
        for i in words[1:]:
            s &= Counter(i)
            
        return list(s.elements())