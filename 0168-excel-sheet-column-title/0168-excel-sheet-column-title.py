class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=""
        while(columnNumber>0):
            columnNumber-=1
            i=columnNumber%26
            res+=chr(65+i)
            columnNumber=columnNumber//26
        return res[::-1]