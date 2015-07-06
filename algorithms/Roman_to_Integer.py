"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        mp={'Z':0,'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500, 'M':1000}
        num=0
        pre='Z'
        flag=1
        for ch in s:
            if(mp[ch]<=mp[pre]):
                flag=1
            else:
                flag=-1
            num+=mp[pre]*flag
            pre=ch
        num+=mp[pre]
        return num
        
                
         #error   没考虑完全。
        # mp={'I':1,'II':2,'III':3,'IV':4,'V':5,
        #          'VI':6,'VII':7,'VIII':8,'IX':9,
        #          'X':10, 'XX':20, 'XXX':30,'XL':40,'L':50,
        #          'LX':60,'LXX':70,'LXXX':80,'XC':90,
        #          'C':100,'CC':200,'CCC':300,'CD':400,'D':500,
        #          'DC':600,'DCC':700,'DCCC':800,'CM':900,
        #          'M':1000,'MM':2000,'MMM':3000
        #     }
        # num=0
        # if (s=="") :
        #      return num
        # fmt=[['M'],['D','C'],['X','L'],['I','V']]
        # fcur=0
        # strlen=len(s)
        # scur=0
        # while(scur<strlen and fcur<4):
        #     tmp=scur
        #     while (s[scur] in fmt[fcur] ):
        #         scur+=1
        #         if (scur>=strlen):
        #             break
        #     if(tmp<scur):    
        #      num+=mp[s[tmp:scur]]
        #     fcur+=1
        # return num
