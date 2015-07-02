"""
program：
 Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""
class Solution:
    # @param {string} s
    # @return {integer}
    #@prelen :前一个字符的最长子串大小：例s="abcdad" ,则s[a]=4, 则对于b来说，只需要比较b为相对地址的第4个即可。
    def lengthOfLongestSubstring(self, s):
        max=1
        prelen=1
        strlen=len(s)
        i=0
        if (strlen ==0):
            return 0
        while(i<strlen-max):
             substr=s[i:i+prelen]
             while(s[i+prelen] not in substr):
                 prelen+=1
                 if max<prelen :
                     max=prelen
                 if (i+prelen >= strlen):
                     return max
                 substr=s[i:i+prelen]
                 
             prelen -= 1
             i+=1
              
        return max
  
