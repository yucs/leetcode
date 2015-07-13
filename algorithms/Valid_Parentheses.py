"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Show Tags
Show Similar Problems

"""

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        mp={'(':')' , '{':'}' , '[':']',' ':' '}
        st=[' ']
        slen=len(s)
        for cur in range(slen):
            if s[cur] in ['[','{','(']:
                st.append(s[cur])
            elif s[cur] in [']','}',')']:
                 if s[cur] !=mp[st.pop()]:
                      return False
        
        if st.pop()!=' ':
            return False
        
        return True
