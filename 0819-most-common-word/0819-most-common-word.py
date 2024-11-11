import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        ban = set(banned)
        
        word_count = Counter(word for word in words if word not in ban)
        m, t = word_count.most_common(1)[0]
        
        return m