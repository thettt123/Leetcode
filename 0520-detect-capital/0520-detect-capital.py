class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or word ==word.lower():
            return True
        elif word[0].isupper() ==True and word[1:].islower()==True:
            return True
        else:
            return False