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
