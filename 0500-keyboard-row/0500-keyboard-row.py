class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        l1, l2, l3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        valid_words = []
        
        for word in words:
            w = set(word.lower())
            
            if w <= l1 or w <= l2 or w <= l3:
                valid_words.append(word)
                
        return valid_words