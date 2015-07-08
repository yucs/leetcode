/*
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
*/
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        string fstr=filter(digits);
        if (fstr.size()<=0){
            // result.push_back("");
            return result;
        }
        string tmp;
        combination(result,digits,tmp,0);
       return  result;
    }
    
    void combination(vector<string>& result,string& digits, string str, int cur){
              // static char* mp[10]={
        //     " ",
        //     "",
        //     "abc",
        //     "def",
        //     "ghi",
        //     "jdl",
        //     "mno",
        //     "pqrs",
        //     "tuv",
        //     "wxyz"
        // };
        static char mp[10][5]={
            {' ', '\0'},
            {'\0'},
            {'a','b','c','\0'},
            {'d','e','f','\0'},
            {'g','h','i','\0'},
            {'j',  'k',  'l',  '\0' }, 
            {'m',  'n',  'o',  '\0' }, 
            {'p',  'q',  'r',  's' ,'\0' }, 
            {'t',  'u',  'v',  '\0' }, 
            {'w',  'x',  'y',  'z'  ,'\0'}  
            
        };
      if(cur>=digits.size()){
          result.push_back(str);
          return ;
      }
      int num=digits[cur]-'0';
      char *scur=&mp[num][0];
      while(*scur){
           string tmp=str+*scur;
           combination(result,digits, tmp,cur+1);
           scur++;
      }
    }
    
    string filter(string& digits){
        string fter;
        for(int i=0;i<digits.size();i++){
            if(!isdigit(digits[i])){
                return "";
            }
            if (digits[i]=='1'){
                continue;
            }else{
                fter+=digits[i];
            }
        }
        return fter;
    }
};
