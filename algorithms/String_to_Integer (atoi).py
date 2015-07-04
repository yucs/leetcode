"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""
class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        if(str==""):
            return 0
        s,flag=self.filter(str)
        result=0
        cur=0
        slen=len(s)
        while(cur<slen):
            result=result*10+int(s[cur])*flag
            cur+=1
            
        return result
            
          
        
        
    # @return {string} 
    # @return {flag}
    def filter(self,str):
        max="2147483647"
        min="2147483648"
        s=""
        flag=1
        ch_flg=True
        ch_w=True
        for ch in str:
            if(ch==' ' and s=="" and ch_flg):
                continue
            
            if((ch=='+' or ch=='-') and ch_flg):
                if (ch=='-'):
                    flag=-1
                ch_flg=False
                continue
                
            if(ch>'9' or ch<'0'):
                break
            
            s+=ch
            
        if (s==""):
            return '0',0
            
        if (len(s)<len(max)):
            return s,flag
            
        if (len(s)==len(max)):
            if ((flag==-1 and s<min )or (flag==1 and s<max)):
                return s,flag
        
        if(flag==-1):
            return min,flag
        else:
            return max,flag
        
