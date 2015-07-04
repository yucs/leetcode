"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        strlen=len(s)
        sum=(numRows-1)*2
        r=""
        if (numRows==1 or strlen==0):
            return s
        for i in range(numRows):
                cur=i
                if(cur==0 or cur==numRows-1):
                    while(cur<strlen):
                        r+=s[cur]
                        cur+=sum
                else:
                    step=sum-cur*2
                    while(cur<strlen):
                        r+=s[cur]
                        cur+=step
                        step=sum-step
        
        return r
