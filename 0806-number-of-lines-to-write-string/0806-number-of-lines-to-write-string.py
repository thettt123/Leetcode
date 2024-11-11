class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        total_line = 1
        width = 0
        
        for char in s:
            char_index = ord(char) - ord('a')
            char_width = widths[char_index]
            
            if width + char_width > 100:
                total_line += 1
                width = char_width
            else:
                width += char_width
        
        return [total_line, width]