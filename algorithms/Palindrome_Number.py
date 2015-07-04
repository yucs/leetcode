"""
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if (x<0):
            return False
        r=0
        cur=x
        while(cur>0):
            r=r*10+cur%10
            cur/=10
        
        if (x==r):
            return True
        else:
            return False
