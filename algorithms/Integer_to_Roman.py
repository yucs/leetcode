"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        mp=[]
        s=""
        mp.append({1:'I',2:'II',3:'III',4:'IV',5:'V',
               6:'VI',7:'VII',8:'VIII',9:'IX'
            })
        mp.append({1:'X',2:'XX',3:'XXX',4:'XL',5:'L',
               6:'LX',7:'LXX',8:'LXXX',9:'XC'
            })
        mp.append({1:'C',2:'CC',3:'CCC',4:'CD',5:'D',
               6:'DC',7:'DCC',8:'DCCC',9:'CM'
            })
        mp.append({1:'M',2:'MM',3:'MMM'})
        snum=str(num)
        leng=len(snum)-1
        for ch in snum:
            if ch=='0':
                leng-=1
                continue
            s+=mp[leng][int(ch)]
            leng-=1
        return s  
