class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        unique_transform = set()
        
        for word in words:
            transform = ''.join(morse[ord(char) - ord('a')] for char in word)
            unique_transform.add(transform)
        
        return len(unique_transform)