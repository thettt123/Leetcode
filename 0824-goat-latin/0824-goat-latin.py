class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        wordlist = sentence.split(' ')
        vowels = ['a','e','o','u','i']
        for i in range(len(wordlist)):
            word = wordlist[i]
            if not word[0].lower() in vowels:
                word = word[1:] + word[0]
            word += 'ma' + (i+1)*'a'
            wordlist[i] = word
        return ' '.join(wordlist)